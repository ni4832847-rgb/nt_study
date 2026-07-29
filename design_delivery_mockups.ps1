Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"

if ($MyInvocation.MyCommand.Path) {
    $root = Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    $root = (Get-Location).Path
}
$outDir = Join-Path $root "delivery_time_designs"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

function ToColor([string]$hex) {
    $hex = $hex.TrimStart("#")
    return [System.Drawing.Color]::FromArgb(
        [Convert]::ToInt32($hex.Substring(0, 2), 16),
        [Convert]::ToInt32($hex.Substring(2, 2), 16),
        [Convert]::ToInt32($hex.Substring(4, 2), 16)
    )
}

function Brush([string]$hex) { return New-Object System.Drawing.SolidBrush -ArgumentList (ToColor $hex) }
function PenC([string]$hex, [float]$w = 1) { return New-Object System.Drawing.Pen -ArgumentList (ToColor $hex), $w }

function RoundedPath($x, $y, $w, $h, $r) {
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $d = $r * 2
    $path.AddArc($x, $y, $d, $d, 180, 90)
    $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $path.CloseFigure()
    return $path
}

function FillRound($g, $x, $y, $w, $h, $r, $hex) {
    if ($r -le 0) {
        $g.FillRectangle((Brush $hex), $x, $y, $w, $h)
        return
    }
    $path = RoundedPath $x $y $w $h $r
    $g.FillPath((Brush $hex), $path)
    $path.Dispose()
}

function StrokeRound($g, $x, $y, $w, $h, $r, $hex, $lw = 1) {
    if ($r -le 0) {
        $g.DrawRectangle((PenC $hex $lw), $x, $y, $w, $h)
        return
    }
    $path = RoundedPath $x $y $w $h $r
    $g.DrawPath((PenC $hex $lw), $path)
    $path.Dispose()
}

function Text($g, $text, $font, $hex, $x, $y, $w = 0, $h = 0, $align = "Near") {
    $fmt = New-Object System.Drawing.StringFormat
    $fmt.Alignment = [System.Drawing.StringAlignment]::$align
    $fmt.LineAlignment = [System.Drawing.StringAlignment]::Near
    $fmt.Trimming = [System.Drawing.StringTrimming]::EllipsisCharacter
    if ($w -gt 0 -and $h -gt 0) {
        $g.DrawString($text, $font, (Brush $hex), [System.Drawing.RectangleF]::new($x, $y, $w, $h), $fmt)
    } else {
        $g.DrawString($text, $font, (Brush $hex), [System.Drawing.PointF]::new($x, $y), $fmt)
    }
    $fmt.Dispose()
}

function ProductImage($g, $x, $y, $kind) {
    FillRound $g $x $y 58 58 29 "#f7f1ec"
    if ($kind -eq "fish") {
        for ($i = 0; $i -lt 5; $i++) {
            $yy = $y + 9 + $i * 8
            $g.DrawLine((PenC "#b77561" 2), $x + 8, $yy, $x + 44, $yy + 4)
            $g.DrawEllipse((PenC "#d7a18d" 1), $x + 12, $yy - 3, 33, 8)
            $g.FillPolygon((Brush "#d18a78"), @(
                [System.Drawing.Point]::new($x + 44, $yy + 4),
                [System.Drawing.Point]::new($x + 53, $yy),
                [System.Drawing.Point]::new($x + 53, $yy + 8)
            ))
        }
    } else {
        for ($i = 0; $i -lt 12; $i++) {
            $px = $x + 10 + (($i * 17) % 38)
            $py = $y + 8 + [Math]::Floor($i / 4) * 13
            $g.FillEllipse((Brush "#c65f20"), $px, $py, 17, 12)
            $g.DrawArc((PenC "#8f3914" 1), $px + 3, $py + 2, 10, 7, 20, 140)
        }
    }
}

function DrawBase($g, $title, $subtitle) {
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.Clear((ToColor "#f5f5f5"))

    $fontTitle = New-Object System.Drawing.Font("Microsoft YaHei UI", 12, [System.Drawing.FontStyle]::Bold)
    $fontNav = New-Object System.Drawing.Font("Microsoft YaHei UI", 8)
    $fontSmall = New-Object System.Drawing.Font("Microsoft YaHei UI", 7)
    $fontSmallB = New-Object System.Drawing.Font("Microsoft YaHei UI", 7, [System.Drawing.FontStyle]::Bold)
    $fontBody = New-Object System.Drawing.Font("Microsoft YaHei UI", 8)
    $fontBodyB = New-Object System.Drawing.Font("Microsoft YaHei UI", 8, [System.Drawing.FontStyle]::Bold)
    $fontBig = New-Object System.Drawing.Font("Microsoft YaHei UI", 11, [System.Drawing.FontStyle]::Bold)

    FillRound $g 0 0 360 590 0 "#ffffff"
    Text $g "<" $fontTitle "#222222" 15 14
    Text $g "我的订单" $fontTitle "#111111" 150 17
    FillRound $g 284 14 56 24 12 "#ffffff"
    StrokeRound $g 284 14 56 24 12 "#eeeeee"
    Text $g "···" $fontBodyB "#111111" 301 15
    Text $g "◎" $fontBodyB "#111111" 326 17

    FillRound $g 26 56 308 30 15 "#f4f4f4"
    Text $g "⌕ 输入商品名称搜索" $fontBody "#9b9b9b" 43 62

    $tabs = @("全部", "待付款", "待发货", "待收货", "已完成")
    $xs = @(35, 92, 156, 220, 284)
    for ($i = 0; $i -lt $tabs.Length; $i++) {
        Text $g $tabs[$i] $fontBody ($(if ($i -eq 0) { "#111111" } else { "#333333" })) $xs[$i] 101
    }
    $g.DrawLine((PenC "#e53e35" 2), 35, 119, 58, 119)

    FillRound $g 10 132 340 332 4 "#ffffff"
    Text $g "▧ 粮农星厨：" $fontSmallB "#333333" 24 146
    Text $g "待发货" $fontSmallB "#e53935" 300 146
    ProductImage $g 26 184 "fish"
    Text $g "加州鲈鱼（4条装）" $fontBodyB "#222222" 108 176
    Text $g "300-350g*4条*8袋" $fontBody "#888888" 108 196
    Text $g "￥322.32元" $fontBody "#222222" 108 229
    Text $g "×1" $fontSmall "#777777" 314 230

    FillRound $g 28 254 304 116 4 "#f7f7f7"
    Text $g "下单时间：" $fontSmall "#777777" 42 265
    Text $g "2026-07-22 12:21:20" $fontSmallB "#333333" 98 265
    Text $g "订单编号：" $fontSmall "#777777" 42 287
    Text $g "2607224356015001" $fontSmallB "#333333" 98 287
    FillRound $g 216 284 27 16 8 "#ffffff"
    Text $g "复制" $fontSmall "#666666" 220 285
    Text $g "配送方式：" $fontSmall "#777777" 42 309
    Text $g "快递配送" $fontSmallB "#333333" 98 309

    Text $g "共1件" $fontSmall "#777777" 246 391
    Text $g "￥312.32" $fontBig "#e53935" 286 386
    StrokeRound $g 207 420 58 24 12 "#dddddd"
    Text $g "再来一单" $fontSmall "#333333" 218 424
    StrokeRound $g 270 420 58 24 12 "#dddddd"
    Text $g "订单详情" $fontSmall "#333333" 280 424

    FillRound $g 10 476 340 100 4 "#ffffff"
    Text $g "▧ 粮农星厨·杭州工厂平台 ›" $fontSmallB "#333333" 24 490
    Text $g "已取消" $fontSmallB "#e53935" 282 490
    ProductImage $g 26 520 "chicken"
    Text $g "2号香卤鸡腿 10个" $fontBodyB "#222222" 108 514
    Text $g "10个*10包" $fontBody "#888888" 108 534

    FillRound $g 12 6 126 32 6 "#ffffff"
    StrokeRound $g 12 6 126 32 6 "#e6e6e6"
    Text $g $title $fontSmallB "#111111" 20 10 110 13
    Text $g $subtitle $fontSmall "#777777" 20 24 110 12

    return @{
        Small=$fontSmall; SmallB=$fontSmallB; Body=$fontBody; BodyB=$fontBodyB; Big=$fontBig; Nav=$fontNav
    }
}

function DrawIconClock($g, $x, $y, $hex) {
    $g.DrawEllipse((PenC $hex 1.8), $x, $y, 13, 13)
    $g.DrawLine((PenC $hex 1.5), $x + 6.5, $y + 3, $x + 6.5, $y + 7)
    $g.DrawLine((PenC $hex 1.5), $x + 6.5, $y + 7, $x + 10, $y + 8.5)
}

function DrawIconTruck($g, $x, $y, $hex) {
    $g.DrawRectangle((PenC $hex 1.5), $x, $y + 3, 16, 9)
    $g.DrawRectangle((PenC $hex 1.5), $x + 16, $y + 6, 8, 6)
    $g.FillEllipse((Brush $hex), $x + 4, $y + 11, 4, 4)
    $g.FillEllipse((Brush $hex), $x + 18, $y + 11, 4, 4)
}

function DrawIconBell($g, $x, $y, $hex) {
    $g.DrawArc((PenC $hex 1.6), $x + 2, $y + 2, 12, 12, 200, 140)
    $g.DrawLine((PenC $hex 1.6), $x + 3, $y + 9, $x + 2, $y + 13)
    $g.DrawLine((PenC $hex 1.6), $x + 13, $y + 9, $x + 14, $y + 13)
    $g.DrawLine((PenC $hex 1.6), $x + 2, $y + 13, $x + 14, $y + 13)
    $g.FillEllipse((Brush $hex), $x + 7, $y + 14, 3, 3)
}

function DrawBaseDeliveryHint($g, $fonts) {
    FillRound $g 42 325 220 28 4 "#fff6ed"
    StrokeRound $g 42 325 220 28 4 "#ffb36a" 1
    DrawIconClock $g 52 333 "#ff6b00"
    Text $g "预计明天送达" $fonts.BodyB "#d94b00" 75 330
}

function ApplyVariant($g, $fonts, $variant) {
    switch ($variant) {
        1 {
            FillRound $g 42 325 270 32 4 "#fff2e8"
            StrokeRound $g 42 325 270 32 4 "#ff7a1a" 1.5
            DrawIconClock $g 54 334 "#ff6b00"
            Text $g "预计明天送达" $fonts.BodyB "#d94b00" 76 331
            Text $g "下单后自动预估，异常及时通知" $fonts.Small "#9b5d28" 172 334
        }
        2 {
            FillRound $g 246 170 84 24 12 "#e53935"
            Text $g "明天送达" $fonts.SmallB "#ffffff" 267 174
            DrawIconTruck $g 252 173 "#ffffff"
            Text $g "配送时效：预计明天送达" $fonts.SmallB "#333333" 42 331
        }
        3 {
            FillRound $g 28 325 304 42 4 "#fff7ed"
            $g.DrawLine((PenC "#ff8a00" 3), 43, 346, 282, 346)
            $g.FillEllipse((Brush "#ff8a00"), 39, 342, 8, 8)
            $g.FillEllipse((Brush "#ff8a00"), 159, 342, 8, 8)
            $g.FillEllipse((Brush "#dddddd"), 279, 342, 8, 8)
            Text $g "已下单" $fonts.Small "#777777" 34 352
            Text $g "明天送达" $fonts.SmallB "#d94b00" 139 352
            Text $g "完成" $fonts.Small "#999999" 273 352
        }
        4 {
            FillRound $g 108 216 148 28 4 "#fff1e6"
            StrokeRound $g 108 216 148 28 4 "#ff9a3d"
            DrawIconTruck $g 119 223 "#ff6b00"
            Text $g "预计明天送达" $fonts.BodyB "#d94b00" 148 221
            Text $g "配送时效：" $fonts.Small "#777777" 42 331
            Text $g "预计明天送达" $fonts.SmallB "#333333" 98 331
        }
        5 {
            FillRound $g 235 143 96 28 14 "#fff0f0"
            StrokeRound $g 235 143 96 28 14 "#ff6b6b"
            Text $g "待发货｜明天达" $fonts.SmallB "#d92d20" 244 150
            Text $g "配送时效：" $fonts.Small "#777777" 42 331
            Text $g "预计明天送达" $fonts.SmallB "#333333" 98 331
        }
        6 {
            FillRound $g 42 325 252 34 4 "#f0f8ff"
            StrokeRound $g 42 325 252 34 4 "#2d8cff"
            Text $g "7/23" $fonts.Big "#1677ff" 55 330
            Text $g "预计送达" $fonts.SmallB "#1677ff" 97 329
            Text $g "明天可送达，注意查收" $fonts.Small "#566b84" 97 344
        }
        7 {
            FillRound $g 28 325 304 39 4 "#f6ffed"
            StrokeRound $g 28 325 304 39 4 "#52c41a"
            DrawIconTruck $g 45 336 "#389e0d"
            Text $g "配送承诺" $fonts.SmallB "#389e0d" 78 330
            Text $g "预计明天送达" $fonts.BodyB "#237804" 78 345
            FillRound $g 255 335 54 20 10 "#ffffff"
            Text $g "准时达" $fonts.SmallB "#237804" 266 338
        }
        8 {
            FillRound $g 28 325 304 34 4 "#ffffff"
            $g.DrawLine((PenC "#eeeeee" 1), 42, 325, 318, 325)
            FillRound $g 42 333 66 18 9 "#ff7a1a"
            Text $g "配送时效" $fonts.SmallB "#ffffff" 52 335
            Text $g "预计明天送达" $fonts.BodyB "#d94b00" 118 331
        }
        9 {
            FillRound $g 28 374 304 34 0 "#fff4e5"
            $g.DrawLine((PenC "#ff8a00" 3), 28, 374, 28, 408)
            DrawIconClock $g 44 384 "#ff6b00"
            Text $g "预计明天送达" $fonts.BodyB "#d94b00" 68 381
            Text $g "后台异常时提醒客服处理" $fonts.Small "#8a5a20" 168 384
        }
        10 {
            FillRound $g 42 324 120 22 11 "#fff1e6"
            Text $g "预计明天送达" $fonts.SmallB "#d94b00" 62 327
            DrawIconClock $g 48 329 "#d94b00"
            Text $g "配送方式：" $fonts.Small "#777777" 42 309
            Text $g "快递配送" $fonts.SmallB "#333333" 98 309
        }
    }
}

function ApplyUrgeVariant($g, $fonts, $variant) {
    DrawBaseDeliveryHint $g $fonts
    switch ($variant) {
        1 {
            StrokeRound $g 144 420 56 24 12 "#ff7a1a" 1.4
            Text $g "催单" $fonts.SmallB "#d94b00" 161 424
            StrokeRound $g 207 420 58 24 12 "#dddddd"
            Text $g "再来一单" $fonts.Small "#333333" 218 424
            StrokeRound $g 270 420 58 24 12 "#dddddd"
            Text $g "订单详情" $fonts.Small "#333333" 280 424
        }
        2 {
            FillRound $g 145 420 58 24 12 "#e53935"
            DrawIconBell $g 154 424 "#ffffff"
            Text $g "催单" $fonts.SmallB "#ffffff" 174 424
            StrokeRound $g 208 420 58 24 12 "#dddddd"
            Text $g "再来一单" $fonts.Small "#333333" 219 424
            StrokeRound $g 270 420 58 24 12 "#dddddd"
            Text $g "订单详情" $fonts.Small "#333333" 280 424
        }
        3 {
            FillRound $g 250 325 68 28 14 "#ff7a1a"
            DrawIconBell $g 260 331 "#ffffff"
            Text $g "催单" $fonts.SmallB "#ffffff" 280 331
        }
        4 {
            FillRound $g 235 143 96 28 14 "#fff0f0"
            StrokeRound $g 235 143 96 28 14 "#ff6b6b"
            DrawIconBell $g 244 149 "#e53935"
            Text $g "催商家发货" $fonts.SmallB "#d92d20" 264 149
        }
        5 {
            FillRound $g 108 216 164 30 4 "#fff1e6"
            StrokeRound $g 108 216 164 30 4 "#ff9a3d"
            DrawIconTruck $g 118 223 "#ff6b00"
            Text $g "明天达" $fonts.BodyB "#d94b00" 145 221
            FillRound $g 214 221 48 20 10 "#ff7a1a"
            Text $g "催单" $fonts.SmallB "#ffffff" 226 224
        }
        6 {
            FillRound $g 285 262 38 38 19 "#ffffff"
            StrokeRound $g 285 262 38 38 19 "#ff7a1a" 1.4
            DrawIconBell $g 296 270 "#ff6b00"
            Text $g "催" $fonts.SmallB "#d94b00" 300 285
        }
        7 {
            FillRound $g 143 420 62 24 12 "#f2f2f2"
            Text $g "已催单" $fonts.SmallB "#999999" 156 424
            Text $g "商家已收到提醒" $fonts.Small "#999999" 142 449
            StrokeRound $g 208 420 58 24 12 "#dddddd"
            Text $g "再来一单" $fonts.Small "#333333" 219 424
            StrokeRound $g 270 420 58 24 12 "#dddddd"
            Text $g "订单详情" $fonts.Small "#333333" 280 424
        }
        8 {
            FillRound $g 28 374 304 34 0 "#fff4e5"
            $g.DrawLine((PenC "#ff8a00" 3), 28, 374, 28, 408)
            Text $g "商家还未发货，可提醒一次" $fonts.SmallB "#8a5a20" 45 383
            FillRound $g 250 381 62 20 10 "#ff7a1a"
            Text $g "催单" $fonts.SmallB "#ffffff" 269 384
        }
        9 {
            StrokeRound $g 133 420 72 24 12 "#2d8cff" 1.2
            Text $g "联系客服" $fonts.Small "#1677ff" 145 424
            FillRound $g 211 420 54 24 12 "#ff7a1a"
            Text $g "催单" $fonts.SmallB "#ffffff" 228 424
            StrokeRound $g 270 420 58 24 12 "#dddddd"
            Text $g "订单详情" $fonts.Small "#333333" 280 424
        }
        10 {
            FillRound $g 42 356 130 22 11 "#ffffff"
            StrokeRound $g 42 356 130 22 11 "#ff7a1a" 1.2
            DrawIconBell $g 51 360 "#ff6b00"
            Text $g "一键催商家发货" $fonts.SmallB "#d94b00" 70 359
            StrokeRound $g 207 420 58 24 12 "#dddddd"
            Text $g "再来一单" $fonts.Small "#333333" 218 424
            StrokeRound $g 270 420 58 24 12 "#dddddd"
            Text $g "订单详情" $fonts.Small "#333333" 280 424
        }
    }
}

$variants = @(
    @{Title="01 信息区高亮"; Subtitle="最稳妥，改动小"},
    @{Title="02 状态旁强提醒"; Subtitle="扫一眼就能看到"},
    @{Title="03 进度条时效"; Subtitle="适合物流心智"},
    @{Title="04 商品下承诺"; Subtitle="贴近商品决策"},
    @{Title="05 状态合并标签"; Subtitle="信息更集中"},
    @{Title="06 日期卡片"; Subtitle="具体日期更明确"},
    @{Title="07 承诺条"; Subtitle="信任感更强"},
    @{Title="08 标签+正文"; Subtitle="弱打扰但清晰"},
    @{Title="09 结算前提醒"; Subtitle="靠近操作区"},
    @{Title="10 轻量胶囊"; Subtitle="最克制的强化"}
)

$w = 360
$h = 590
$gap = 18
$sheetW = $w * 2 + $gap * 3
$sheetH = $h * 5 + $gap * 6
$sheet = New-Object System.Drawing.Bitmap($sheetW, $sheetH)
$sg = [System.Drawing.Graphics]::FromImage($sheet)
$sg.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$sg.Clear((ToColor "#e9e9e9"))

for ($i = 0; $i -lt $variants.Count; $i++) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $fonts = DrawBase $g $variants[$i].Title $variants[$i].Subtitle
    ApplyVariant $g $fonts ($i + 1)
    $file = Join-Path $outDir ("delivery_time_style_{0:D2}.png" -f ($i + 1))
    $bmp.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)

    $col = $i % 2
    $row = [Math]::Floor($i / 2)
    $x = $gap + $col * ($w + $gap)
    $y = $gap + $row * ($h + $gap)
    $sg.DrawImage($bmp, $x, $y, $w, $h)

    $g.Dispose()
    $bmp.Dispose()
}

$sheetFile = Join-Path $outDir "delivery_time_10_styles_contact_sheet.png"
$sheet.Save($sheetFile, [System.Drawing.Imaging.ImageFormat]::Png)
$sg.Dispose()
$sheet.Dispose()

Write-Host $sheetFile

$urgeDir = Join-Path $root "urge_button_designs"
New-Item -ItemType Directory -Force -Path $urgeDir | Out-Null

$urgeVariants = @(
    @{Title="01 底部弱主按钮"; Subtitle="推荐：符合操作习惯"},
    @{Title="02 底部强主按钮"; Subtitle="最明显，适合急单"},
    @{Title="03 时效旁催单"; Subtitle="原因和动作贴近"},
    @{Title="04 状态旁入口"; Subtitle="靠近待发货状态"},
    @{Title="05 商品区按钮"; Subtitle="贴近当前商品"},
    @{Title="06 侧边悬浮"; Subtitle="强提醒但需克制"},
    @{Title="07 已催单状态"; Subtitle="避免重复点击"},
    @{Title="08 提醒条按钮"; Subtitle="解释后再操作"},
    @{Title="09 客服+催单"; Subtitle="售后动作组合"},
    @{Title="10 轻量长胶囊"; Subtitle="低打扰的引导"}
)

$urgeSheet = New-Object System.Drawing.Bitmap($sheetW, $sheetH)
$ug = [System.Drawing.Graphics]::FromImage($urgeSheet)
$ug.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$ug.Clear((ToColor "#e9e9e9"))

for ($i = 0; $i -lt $urgeVariants.Count; $i++) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $fonts = DrawBase $g $urgeVariants[$i].Title $urgeVariants[$i].Subtitle
    ApplyUrgeVariant $g $fonts ($i + 1)
    $file = Join-Path $urgeDir ("urge_button_style_{0:D2}.png" -f ($i + 1))
    $bmp.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)

    $col = $i % 2
    $row = [Math]::Floor($i / 2)
    $x = $gap + $col * ($w + $gap)
    $y = $gap + $row * ($h + $gap)
    $ug.DrawImage($bmp, $x, $y, $w, $h)

    $g.Dispose()
    $bmp.Dispose()
}

$urgeSheetFile = Join-Path $urgeDir "urge_button_10_styles_contact_sheet.png"
$urgeSheet.Save($urgeSheetFile, [System.Drawing.Imaging.ImageFormat]::Png)
$ug.Dispose()
$urgeSheet.Dispose()

Write-Host $urgeSheetFile
