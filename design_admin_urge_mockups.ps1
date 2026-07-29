Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = "Stop"

if ($MyInvocation.MyCommand.Path) {
    $root = Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    $root = (Get-Location).Path
}

$outDir = Join-Path $root "admin_urge_record_designs"
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
    if ($r -le 0) {
        $path.AddRectangle([System.Drawing.RectangleF]::new($x, $y, $w, $h))
        return $path
    }
    $d = $r * 2
    $path.AddArc($x, $y, $d, $d, 180, 90)
    $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $path.CloseFigure()
    return $path
}

function FillRound($g, $x, $y, $w, $h, $r, $hex) {
    $path = RoundedPath $x $y $w $h $r
    $g.FillPath((Brush $hex), $path)
    $path.Dispose()
}

function StrokeRound($g, $x, $y, $w, $h, $r, $hex, $lw = 1) {
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

function ProductThumb($g, $x, $y) {
    FillRound $g $x $y 42 42 21 "#fff4ea"
    for ($i = 0; $i -lt 7; $i++) {
        $px = $x + 8 + (($i * 13) % 24)
        $py = $y + 8 + [Math]::Floor($i / 3) * 11
        $g.FillEllipse((Brush "#bc5a1d"), $px, $py, 14, 10)
        $g.DrawArc((PenC "#873914" 1), $px + 3, $py + 2, 8, 6, 20, 140)
    }
}

function DrawButton($g, $x, $y, $w, $h, $text, $mode, $fonts) {
    if ($mode -eq "primary") {
        FillRound $g $x $y $w $h 3 "#1677ff"
        Text $g $text $fonts.SmallB "#ffffff" ($x + 10) ($y + 5) ($w - 20) 16 "Center"
    } elseif ($mode -eq "danger") {
        FillRound $g $x $y $w $h 3 "#ff4d4f"
        Text $g $text $fonts.SmallB "#ffffff" ($x + 10) ($y + 5) ($w - 20) 16 "Center"
    } elseif ($mode -eq "orange") {
        FillRound $g $x $y $w $h 3 "#ff7a1a"
        Text $g $text $fonts.SmallB "#ffffff" ($x + 10) ($y + 5) ($w - 20) 16 "Center"
    } else {
        FillRound $g $x $y $w $h 3 "#ffffff"
        StrokeRound $g $x $y $w $h 3 "#d9d9d9"
        Text $g $text $fonts.Small "#333333" ($x + 8) ($y + 5) ($w - 16) 16 "Center"
    }
}

function DrawInput($g, $x, $y, $w, $label, $value, $fonts) {
    Text $g $label $fonts.Small "#333333" $x ($y + 7) 76 14
    FillRound $g ($x + 72) $y $w 28 3 "#ffffff"
    StrokeRound $g ($x + 72) $y $w 28 3 "#d9dfe8"
    Text $g $value $fonts.Small "#8c8c8c" ($x + 84) ($y + 7) ($w - 24) 14
}

function DrawAdminBase($g, $title, $subtitle) {
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.Clear((ToColor "#f3f5f8"))

    $fontLogo = New-Object System.Drawing.Font("Microsoft YaHei UI", 12, [System.Drawing.FontStyle]::Bold)
    $fontTitle = New-Object System.Drawing.Font("Microsoft YaHei UI", 13, [System.Drawing.FontStyle]::Bold)
    $fontBody = New-Object System.Drawing.Font("Microsoft YaHei UI", 9)
    $fontBodyB = New-Object System.Drawing.Font("Microsoft YaHei UI", 9, [System.Drawing.FontStyle]::Bold)
    $fontSmall = New-Object System.Drawing.Font("Microsoft YaHei UI", 7.5)
    $fontSmallB = New-Object System.Drawing.Font("Microsoft YaHei UI", 7.5, [System.Drawing.FontStyle]::Bold)
    $fontBig = New-Object System.Drawing.Font("Microsoft YaHei UI", 18, [System.Drawing.FontStyle]::Bold)

    $fonts = @{Logo=$fontLogo; Title=$fontTitle; Body=$fontBody; BodyB=$fontBodyB; Small=$fontSmall; SmallB=$fontSmallB; Big=$fontBig}

    FillRound $g 0 0 1366 768 0 "#f3f5f8"
    FillRound $g 0 0 1366 46 0 "#ffffff"
    StrokeRound $g 0 45 1366 1 0 "#e8edf3"
    Text $g "饭圈粮农鲜配·商家端" $fontLogo "#222222" 18 13
    Text $g "客服" $fontSmall "#4f6b95" 1240 16
    Text $g "粮农星厨" $fontSmall "#4f6b95" 1280 16

    FillRound $g 0 46 56 722 0 "#1f1f1f"
    $navs = @("首页", "店铺", "库存", "商品", "营销", "订单", "客户", "数据", "客服", "系统")
    for ($i = 0; $i -lt $navs.Length; $i++) {
        $yy = 70 + $i * 46
        if ($navs[$i] -eq "订单") { FillRound $g 0 ($yy - 8) 56 36 0 "#1677ff" }
        Text $g $navs[$i] $fontSmall "#ffffff" 18 $yy
    }

    FillRound $g 56 46 78 722 0 "#ffffff"
    Text $g "订单管理" $fontBodyB "#333333" 72 72
    Text $g "订单查询" $fontSmallB "#1677ff" 72 112
    Text $g "核销记录" $fontSmall "#333333" 72 152
    Text $g "退货退款" $fontSmall "#333333" 72 192
    Text $g "配送管理" $fontSmall "#333333" 72 232

    FillRound $g 134 46 1232 54 0 "#ffffff"
    Text $g "订单 / 订单管理 / 订单查询" $fontSmall "#7b8aa0" 158 66

    FillRound $g 147 116 1195 112 0 "#ffffff"
    DrawInput $g 168 142 146 "订单编号：" "请输入订单编号" $fonts
    DrawInput $g 386 142 146 "订单状态：" "待发货" $fonts
    DrawInput $g 604 142 146 "催单状态：" "全部" $fonts
    DrawInput $g 822 142 146 "收件人：" "请输入姓名" $fonts
    DrawInput $g 1040 142 146 "手机号：" "请输入手机号" $fonts
    DrawInput $g 168 180 146 "下单时间：" "开始日期  至  结束日期" $fonts
    DrawButton $g 604 180 56 28 "搜索" "primary" $fonts
    DrawButton $g 670 180 72 28 "重置" "default" $fonts
    DrawButton $g 752 180 88 28 "批量发货" "default" $fonts

    FillRound $g 147 246 1195 36 0 "#ffffff"
    $tabs = @("全部", "待付款", "待发货", "待收货", "交易成功", "催单订单")
    $tx = 168
    foreach ($tab in $tabs) {
        $color = "#333333"
        if ($tab -eq "待发货") { $color = "#1677ff" }
        Text $g $tab $fontSmallB $color $tx 258
        $tx += 72
    }
    $g.DrawLine((PenC "#1677ff" 2), 304, 280, 344, 280)

    FillRound $g 147 292 1195 34 0 "#fafafa"
    Text $g "商品" $fontSmallB "#333333" 168 304
    Text $g "成交单价/数量" $fontSmallB "#333333" 620 304
    Text $g "实付金额" $fontSmallB "#333333" 760 304
    Text $g "买家/收货人" $fontSmallB "#333333" 910 304
    Text $g "订单状态" $fontSmallB "#333333" 1080 304
    Text $g "催单信息" $fontSmallB "#333333" 1180 304
    Text $g "操作" $fontSmallB "#333333" 1290 304

    $rows = @(
        @{No="2607214208004001"; Time="2026-07-21 16:26:10"; Goods="肉末茄子 200g 200g*10包"; User="张鑫`n180****1615"; Urge="今日2/3  总3次"; Last="07-22 10:18"; Status="待处理"},
        @{No="2607214208003001"; Time="2026-07-21 16:25:34"; Goods="加州鲈鱼 300-350g*4条"; User="李明`n139****4820"; Urge="今日1/3  总1次"; Last="07-22 09:42"; Status="已处理"},
        @{No="2607164207001001"; Time="2026-07-16 14:28:36"; Goods="茄子红烧肉 200g 200g*1包"; User="王珊`n186****7231"; Urge="今日3/3  总5次"; Last="07-22 11:03"; Status="已超限"}
    )
    $y = 326
    foreach ($r in $rows) {
        FillRound $g 147 $y 1195 122 0 "#ffffff"
        StrokeRound $g 147 $y 1195 122 0 "#edf0f5"
        FillRound $g 147 $y 1195 28 0 "#fbfcfe"
        Text $g ("订单编号:" + $r.No + "    下单时间:" + $r.Time + "    用户编码:48001    门店编码:1000027034") $fontSmallB "#2f3a4a" 156 ($y + 8)
        ProductThumb $g 164 ($y + 47)
        Text $g $r.Goods $fontSmall "#475569" 218 ($y + 53) 230 18
        FillRound $g 218 ($y + 78) 40 18 2 "#fff1f0"
        StrokeRound $g 218 ($y + 78) 40 18 2 "#ff4d4f"
        Text $g "待发货" $fontSmall "#ff4d4f" 226 ($y + 80)
        Text $g "0.01`n1件" $fontSmall "#475569" 636 ($y + 50) 60 34 "Center"
        Text $g "0.01元`n共1件" $fontSmallB "#f04438" 770 ($y + 50) 80 34 "Center"
        Text $g $r.User $fontSmall "#475569" 916 ($y + 48) 90 36 "Center"
        Text $g "待发货" $fontSmall "#475569" 1086 ($y + 58) 80 18 "Center"
        Text $g $r.Urge $fontSmallB "#d4380d" 1174 ($y + 46) 100 16 "Center"
        Text $g ("最近 " + $r.Last) $fontSmall "#8c8c8c" 1174 ($y + 66) 100 16 "Center"
        Text $g $r.Status $fontSmall "#1677ff" 1290 ($y + 44)
        Text $g "催单记录" $fontSmall "#1677ff" 1282 ($y + 66)
        Text $g "发货" $fontSmall "#1677ff" 1296 ($y + 88)
        $y += 132
    }

    FillRound $g 149 12 184 28 4 "#ffffff"
    StrokeRound $g 149 12 184 28 4 "#d9dfe8"
    Text $g $title $fontSmallB "#111111" 160 16 80 14
    Text $g $subtitle $fontSmall "#7b8aa0" 238 16 82 14

    return $fonts
}

function DrawStatCard($g, $x, $y, $w, $title, $value, $hint, $color, $fonts) {
    FillRound $g $x $y $w 74 4 "#ffffff"
    StrokeRound $g $x $y $w 74 4 "#e7ebf0"
    Text $g $title $fonts.Small "#637083" ($x + 16) ($y + 12)
    Text $g $value $fonts.Big $color ($x + 16) ($y + 30)
    Text $g $hint $fonts.Small "#8c8c8c" ($x + 78) ($y + 42)
}

function ApplyAdminVariant($g, $fonts, $variant) {
    switch ($variant) {
        1 {
            FillRound $g 1170 330 110 26 13 "#fff2e8"
            Text $g "客户已催 2/3" $fonts.SmallB "#d46b08" 1188 336
            FillRound $g 1170 462 110 26 13 "#fff7e6"
            Text $g "客户已催 1/3" $fonts.SmallB "#d46b08" 1188 468
            FillRound $g 1170 594 110 26 13 "#fff1f0"
            Text $g "今日已满 3/3" $fonts.SmallB "#cf1322" 1188 600
        }
        2 {
            DrawStatCard $g 147 236 190 "今日催单订单" "8" "待处理5单" "#ff4d4f" $fonts
            DrawStatCard $g 351 236 190 "超限点击" "3" "自动拦截" "#fa8c16" $fonts
            DrawStatCard $g 555 236 190 "平均响应" "18m" "建议30分钟内处理" "#1677ff" $fonts
            FillRound $g 760 236 310 74 4 "#ffffff"
            Text $g "规则：每单每日最多 3 次，间隔 30 分钟；超过后前端按钮置灰。" $fonts.SmallB "#3f4a5f" 782 260 260 36
        }
        3 {
            FillRound $g 968 312 374 410 4 "#ffffff"
            StrokeRound $g 968 312 374 410 4 "#d9dfe8"
            Text $g "催单记录" $fonts.BodyB "#111111" 990 330
            Text $g "订单 2607214208004001" $fonts.Small "#637083" 990 354
            $ys = @(392, 462, 532)
            $texts = @("10:18 客户第2次催单，原因：等待发货", "09:47 系统提醒商家，处理人：客服小李", "09:42 客户第1次催单，来源：小程序")
            for ($i = 0; $i -lt 3; $i++) {
                $g.FillEllipse((Brush "#1677ff"), 994, $ys[$i], 8, 8)
                $g.DrawLine((PenC "#d9dfe8" 1), 998, ($ys[$i] + 10), 998, ($ys[$i] + 58))
                Text $g $texts[$i] $fonts.Small "#334155" 1016 ($ys[$i] - 4) 250 18
                Text $g "今日次数：2/3    总次数：3" $fonts.Small "#8c8c8c" 1016 ($ys[$i] + 18)
            }
            DrawButton $g 990 654 82 28 "标记已处理" "primary" $fonts
            DrawButton $g 1084 654 82 28 "联系买家" "default" $fonts
        }
        4 {
            FillRound $g 147 326 1195 46 0 "#fff7e6"
            $g.DrawLine((PenC "#fa8c16" 3), 147, 326, 147, 372)
            Text $g "催单提醒：客户今日已催 2 次，上次催单 10:18，建议优先发货或联系买家说明时效。" $fonts.BodyB "#ad4e00" 168 340
            DrawButton $g 1170 335 80 28 "处理催单" "orange" $fonts
            DrawButton $g 1260 335 62 28 "展开" "default" $fonts
        }
        5 {
            FillRound $g 426 252 90 22 11 "#fff1f0"
            Text $g "催单订单 8" $fonts.SmallB "#cf1322" 440 256
            FillRound $g 1168 330 92 22 11 "#fff1f0"
            Text $g "待处理" $fonts.SmallB "#cf1322" 1194 334
            FillRound $g 1168 462 92 22 11 "#f6ffed"
            Text $g "已回复" $fonts.SmallB "#389e0d" 1194 466
            FillRound $g 1168 594 92 22 11 "#f5f5f5"
            Text $g "已超限" $fonts.SmallB "#8c8c8c" 1194 598
        }
        6 {
            FillRound $g 147 236 1195 68 4 "#ffffff"
            Text $g "催单看板" $fonts.BodyB "#111111" 168 252
            Text $g "把客户催单作为待办处理，而不是只在订单详情里查看。" $fonts.Small "#637083" 168 276
            DrawButton $g 1030 256 88 28 "只看催单" "primary" $fonts
            DrawButton $g 1128 256 88 28 "批量提醒" "orange" $fonts
            DrawButton $g 1226 256 88 28 "导出记录" "default" $fonts
        }
        7 {
            FillRound $g 1176 338 84 24 12 "#fff2e8"
            Text $g "2/3 次" $fonts.SmallB "#d46b08" 1204 342
            Text $g "剩余1次" $fonts.Small "#8c8c8c" 1194 366
            FillRound $g 1176 470 84 24 12 "#e6f4ff"
            Text $g "1/3 次" $fonts.SmallB "#1677ff" 1204 474
            Text $g "剩余2次" $fonts.Small "#8c8c8c" 1194 498
            FillRound $g 1176 602 84 24 12 "#f5f5f5"
            Text $g "3/3 次" $fonts.SmallB "#8c8c8c" 1204 606
            Text $g "明天恢复" $fonts.Small "#8c8c8c" 1190 630
        }
        8 {
            FillRound $g 1018 116 324 610 4 "#ffffff"
            StrokeRound $g 1018 116 324 610 4 "#d9dfe8"
            Text $g "催单设置" $fonts.BodyB "#111111" 1040 138
            Text $g "前端限制" $fonts.SmallB "#637083" 1040 176
            Text $g "每单每天可点次数" $fonts.Small "#333333" 1040 206
            FillRound $g 1182 198 52 28 3 "#ffffff"
            StrokeRound $g 1182 198 52 28 3 "#d9dfe8"
            Text $g "3" $fonts.BodyB "#111111" 1204 203
            Text $g "两次催单间隔" $fonts.Small "#333333" 1040 246
            FillRound $g 1182 238 72 28 3 "#ffffff"
            StrokeRound $g 1182 238 72 28 3 "#d9dfe8"
            Text $g "30分钟" $fonts.SmallB "#111111" 1196 246
            Text $g "超限提示文案" $fonts.Small "#333333" 1040 286
            FillRound $g 1040 316 254 44 3 "#f8fafc"
            Text $g "今日催单次数已用完，明天可继续提醒商家。" $fonts.Small "#475569" 1052 328 224 22
            DrawButton $g 1040 390 82 28 "保存规则" "primary" $fonts
        }
        9 {
            FillRound $g 147 326 1195 122 0 "#ffffff"
            FillRound $g 934 356 322 64 4 "#fff7ed"
            StrokeRound $g 934 356 322 64 4 "#fdba74"
            Text $g "催单摘要" $fonts.SmallB "#9a3412" 954 370
            Text $g "今日第2次 / 总第3次 / 距上次31分钟 / 待客服处理" $fonts.Small "#9a3412" 954 394 260 16
            DrawButton $g 1266 374 54 28 "处理" "orange" $fonts
        }
        10 {
            FillRound $g 147 236 1195 64 4 "#ffffff"
            Text $g "新增字段建议" $fonts.BodyB "#111111" 168 252
            Text $g "订单列表展示：今日催单次数、总催单次数、最近催单时间、最近催单来源、处理状态、处理人。" $fonts.Small "#475569" 168 278
            FillRound $g 147 326 1195 122 0 "#ffffff"
            $headers = @("订单编号", "买家", "今日/上限", "总次数", "最近催单", "来源", "处理状态", "处理人", "操作")
            $xs = @(170, 340, 470, 590, 700, 835, 940, 1060, 1180)
            for ($i = 0; $i -lt $headers.Length; $i++) { Text $g $headers[$i] $fonts.SmallB "#334155" $xs[$i] 350 }
            Text $g "2607214208004001" $fonts.Small "#475569" 170 392
            Text $g "张鑫 180****1615" $fonts.Small "#475569" 340 392
            Text $g "2/3" $fonts.SmallB "#d46b08" 480 392
            Text $g "3" $fonts.Small "#475569" 604 392
            Text $g "2026-07-22 10:18" $fonts.Small "#475569" 700 392
            Text $g "小程序" $fonts.Small "#475569" 840 392
            Text $g "待处理" $fonts.SmallB "#cf1322" 948 392
            Text $g "未分配" $fonts.Small "#8c8c8c" 1064 392
            DrawButton $g 1180 384 78 28 "查看记录" "primary" $fonts
        }
    }
}

$variants = @(
    @{Title="01 列表字段增强"; Subtitle="最稳，开发成本低"},
    @{Title="02 顶部统计+规则"; Subtitle="管理者更好看"},
    @{Title="03 右侧记录抽屉"; Subtitle="详情信息完整"},
    @{Title="04 行内提醒条"; Subtitle="异常优先处理"},
    @{Title="05 催单订单标签"; Subtitle="筛选效率高"},
    @{Title="06 催单看板入口"; Subtitle="适合客服待办"},
    @{Title="07 次数胶囊"; Subtitle="次数最直观"},
    @{Title="08 规则设置面板"; Subtitle="配置每日次数"},
    @{Title="09 行内摘要卡"; Subtitle="无需打开详情"},
    @{Title="10 独立记录表"; Subtitle="数据最规范"}
)

$w = 1366
$h = 768
$gap = 24
$sheetW = 1366 * 2 + $gap * 3
$sheetH = 768 * 5 + $gap * 6
$sheet = New-Object System.Drawing.Bitmap($sheetW, $sheetH)
$sg = [System.Drawing.Graphics]::FromImage($sheet)
$sg.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$sg.Clear((ToColor "#e6e9ef"))

for ($i = 0; $i -lt $variants.Count; $i++) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $fonts = DrawAdminBase $g $variants[$i].Title $variants[$i].Subtitle
    ApplyAdminVariant $g $fonts ($i + 1)
    $file = Join-Path $outDir ("admin_urge_record_style_{0:D2}.png" -f ($i + 1))
    $bmp.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)

    $col = $i % 2
    $row = [Math]::Floor($i / 2)
    $x = $gap + $col * ($w + $gap)
    $y = $gap + $row * ($h + $gap)
    $sg.DrawImage($bmp, $x, $y, $w, $h)

    $g.Dispose()
    $bmp.Dispose()
}

$sheetFile = Join-Path $outDir "admin_urge_record_10_styles_contact_sheet.png"
$sheet.Save($sheetFile, [System.Drawing.Imaging.ImageFormat]::Png)
$sg.Dispose()
$sheet.Dispose()

Write-Host $sheetFile
