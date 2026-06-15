# """
# ChiefAI — Startup Intelligence Platform
# PDF Export Service

# Generates a polished, judge-ready PDF report containing only the
# information that is shown in the ChiefAI dashboard UI:
#   - Cover / scorecard (overall score, outlook, risk, funding stage, raise)
#   - Executive Summary
#   - Market Analysis (size, growth, TAM/SAM/SOM, competitors, trends,
#     opportunities, risks)
#   - SWOT Snapshot
#   - Business Strategy
#   - Investor Readiness (readiness score, strengths, weaknesses, risks,
#     recommendations)

# No internal AI-agent execution metadata (agent names, execution times,
# agent counts) is included, matching the public-facing dashboard.
# """

# import json
# from datetime import datetime

# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     Table,
#     TableStyle,
#     PageBreak,
#     HRFlowable,
# )
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm
# from reportlab.lib.enums import TA_CENTER, TA_LEFT

# from app.database.db import get_connection


# # ── Brand Palette (Fluent-inspired) ────────────────────────────────────────────

# BLUE         = colors.HexColor("#0078D4")
# BLUE_DARK    = colors.HexColor("#005A9E")
# BLUE_LIGHT   = colors.HexColor("#E5F1FB")
# TEAL         = colors.HexColor("#50E6FF")
# PURPLE       = colors.HexColor("#8764B8")
# GREEN        = colors.HexColor("#107C10")
# GREEN_LIGHT  = colors.HexColor("#DFF6DD")
# ORANGE       = colors.HexColor("#FF8C00")
# ORANGE_LIGHT = colors.HexColor("#FFF4CE")
# RED          = colors.HexColor("#D13438")
# RED_LIGHT    = colors.HexColor("#FDE7E9")
# GRAY_TEXT    = colors.HexColor("#605E5C")
# GRAY_DARK    = colors.HexColor("#323130")
# GRAY_BG      = colors.HexColor("#F3F2F1")
# GRAY_BORDER  = colors.HexColor("#E1DFDD")
# WHITE        = colors.white

# PAGE_W, PAGE_H = A4
# MARGIN = 18 * mm


# # ── Style Builder ──────────────────────────────────────────────────────────────

# def build_styles():
#     styles = getSampleStyleSheet()

#     def add(name, **kw):
#         styles.add(ParagraphStyle(name=name, **kw))

#     add("ChiefTitle",
#         fontName="Helvetica-Bold", fontSize=28, textColor=WHITE,
#         leading=34, spaceAfter=2, alignment=TA_LEFT)

#     add("ChiefSubtitle",
#         fontName="Helvetica", fontSize=12, textColor=colors.HexColor("#C7E0F4"),
#         leading=16, spaceAfter=0, alignment=TA_LEFT)

#     add("SectionHeader",
#         fontName="Helvetica-Bold", fontSize=14, textColor=BLUE_DARK,
#         leading=18, spaceBefore=14, spaceAfter=6, alignment=TA_LEFT)

#     add("SubHeader",
#         fontName="Helvetica-Bold", fontSize=10.5, textColor=GRAY_DARK,
#         leading=14, spaceBefore=6, spaceAfter=3, alignment=TA_LEFT)

#     add("Body",
#         fontName="Helvetica", fontSize=9.5, textColor=GRAY_DARK,
#         leading=14, spaceAfter=3, alignment=TA_LEFT)

#     add("BodySmall",
#         fontName="Helvetica", fontSize=8.5, textColor=GRAY_TEXT,
#         leading=12, spaceAfter=2, alignment=TA_LEFT)

#     add("KpiValue",
#         fontName="Helvetica-Bold", fontSize=22, textColor=GRAY_DARK,
#         leading=26, spaceAfter=2, alignment=TA_CENTER)

#     add("KpiLabel",
#         fontName="Helvetica-Bold", fontSize=7.5, textColor=GRAY_TEXT,
#         leading=10, spaceAfter=0, alignment=TA_CENTER)

#     add("CoverScore",
#         fontName="Helvetica-Bold", fontSize=46, textColor=WHITE,
#         leading=52, alignment=TA_CENTER)

#     add("CoverScoreSub",
#         fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#C7E0F4"),
#         leading=14, alignment=TA_CENTER)

#     add("CoverTag",
#         fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
#         leading=11, spaceAfter=0, alignment=TA_CENTER)

#     return styles


# # ── Table Style Factories ───────────────────────────────────────────────────────

# def std_table_style(header_bg=BLUE, alt_row=BLUE_LIGHT):
#     return TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, 0), header_bg),
#         ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
#         ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
#         ("FONTSIZE",      (0, 0), (-1, 0), 9),
#         ("TOPPADDING",    (0, 0), (-1, 0), 9),
#         ("BOTTOMPADDING", (0, 0), (-1, 0), 9),
#         ("ALIGN",         (0, 0), (-1, 0), "LEFT"),
#         ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
#         ("FONTSIZE",      (0, 1), (-1, -1), 9),
#         ("TOPPADDING",    (0, 1), (-1, -1), 7),
#         ("BOTTOMPADDING", (0, 1), (-1, -1), 7),
#         ("TEXTCOLOR",     (0, 1), (-1, -1), GRAY_DARK),
#         ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, alt_row]),
#         ("LINEBELOW",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#     ])


# def two_col_detail_style():
#     return TableStyle([
#         ("BACKGROUND",    (0, 0), (0, -1), GRAY_BG),
#         ("FONTNAME",      (0, 0), (0, -1), "Helvetica-Bold"),
#         ("FONTSIZE",      (0, 0), (-1, -1), 9),
#         ("TEXTCOLOR",     (0, 0), (0, -1), BLUE_DARK),
#         ("TEXTCOLOR",     (1, 0), (1, -1), GRAY_DARK),
#         ("FONTNAME",      (1, 0), (1, -1), "Helvetica"),
#         ("TOPPADDING",    (0, 0), (-1, -1), 8),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
#         ("LINEBELOW",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ])


# # ── Helpers ───────────────────────────────────────────────────────────────────

# def v(d: dict, key: str, default="Not available") -> str:
#     val = d.get(key, default)
#     if val is None or val == "":
#         return default
#     return str(val)


# def fmt_dt(s) -> str:
#     if not s:
#         return "-"
#     try:
#         return datetime.fromisoformat(str(s)).strftime("%B %d, %Y  %H:%M")
#     except Exception:
#         return str(s)


# def score_color(n: float):
#     if n >= 75: return GREEN
#     if n >= 50: return ORANGE
#     return RED


# def risk_color(risk: str):
#     r = (risk or "").lower()
#     if "low" in r: return GREEN
#     if "medium" in r or "moderate" in r: return ORANGE
#     if "high" in r: return RED
#     return GRAY_TEXT


# def decision_from_score(score: float):
#     if score >= 75: return ("STRONG INVEST", GREEN)
#     if score >= 50: return ("CONSIDER INVEST", ORANGE)
#     return ("NEEDS IMPROVEMENT", RED)


# def section_title(title: str, icon: str, styles) -> list:
#     return [
#         HRFlowable(width="100%", thickness=0.5, color=GRAY_BORDER, spaceAfter=6),
#         Paragraph(f'<font color="#0078D4">\u25A0</font>  {title}', styles["SectionHeader"]),
#         Spacer(1, 4),
#     ]


# def bullet_list(items, style, prefix="  \u2022  ") -> list:
#     if not items:
#         return [Paragraph(f"{prefix}No data available.", style)]
#     return [Paragraph(f"{prefix}{item}", style) for item in items]


# def list_cell(title, items, fg, styles):
#     lines = [Paragraph(f'<b><font color="#{fg.hexval()[2:]}">{title}</font></b>', styles["SubHeader"])]
#     if items:
#         for it in items:
#             lines.append(Paragraph(f'  \u2022  {it}', styles["BodySmall"]))
#     else:
#         lines.append(Paragraph("  \u2022  No data available.", styles["BodySmall"]))
#     return lines


# # ── SWOT 2x2 ──────────────────────────────────────────────────────────────────

# def build_swot_table(swot: dict, styles) -> Table:
#     s_items  = swot.get("strengths", [])
#     w_items  = swot.get("weaknesses", [])
#     o_items  = swot.get("opportunities", [])
#     t_items  = swot.get("threats", [])

#     col_w = (PAGE_W - 2 * MARGIN) / 2

#     t = Table([
#         [list_cell("STRENGTHS", s_items, GREEN, styles), list_cell("WEAKNESSES", w_items, RED, styles)],
#         [list_cell("OPPORTUNITIES", o_items, BLUE, styles), list_cell("THREATS", t_items, ORANGE, styles)],
#     ], colWidths=[col_w, col_w])

#     t.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
#         ("BACKGROUND",    (1, 0), (1, 0), RED_LIGHT),
#         ("BACKGROUND",    (0, 1), (0, 1), BLUE_LIGHT),
#         ("BACKGROUND",    (1, 1), (1, 1), ORANGE_LIGHT),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (0, -1), 0.6, GRAY_BORDER),
#         ("LINEBELOW",     (0, 0), (-1, 0), 0.6, GRAY_BORDER),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 10),
#         ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ]))
#     return t


# # ── Competitor Table ──────────────────────────────────────────────────────────

# def build_competitor_table(competitors: list, styles):
#     if not competitors:
#         return Paragraph("No competitors identified.", styles["BodySmall"])

#     rows = [[
#         Paragraph("<b>#</b>", styles["Body"]),
#         Paragraph("<b>Competitor</b>", styles["Body"]),
#         Paragraph("<b>Key Strength</b>", styles["Body"]),
#     ]]
#     for i, c in enumerate(competitors, start=1):
#         if isinstance(c, dict):
#             name     = c.get("name", "-")
#             strength = c.get("strength", "-")
#         else:
#             name, strength = str(c), "-"
#         rows.append([
#             Paragraph(str(i), styles["Body"]),
#             Paragraph(f'<b><font color="#0078D4">{name}</font></b>', styles["Body"]),
#             Paragraph(strength, styles["BodySmall"]),
#         ])

#     t = Table(rows, colWidths=[25, 160, PAGE_W - 2 * MARGIN - 185])
#     t.setStyle(std_table_style())
#     return t


# # ── Header / Footer (drawn on every page, with ChiefAI logo) ──────────────────

# def draw_chiefai_logo(canv, x, y, size=9):
#     """Draw the ChiefAI multi-agent network mark (matches the app logo)."""
#     canv.saveState()

#     # Connection lines
#     canv.setStrokeColor(colors.HexColor("#7FD6FF"))
#     canv.setLineWidth(0.8)
#     top    = (x, y + size)
#     left   = (x - size * 0.85, y - size * 0.55)
#     right  = (x + size * 0.85, y - size * 0.55)
#     canv.line(top[0], top[1], left[0], left[1])
#     canv.line(top[0], top[1], right[0], right[1])
#     canv.line(left[0], left[1], right[0], right[1])

#     # Nodes
#     canv.setFillColor(BLUE)
#     canv.circle(top[0], top[1], size * 0.32, stroke=0, fill=1)
#     canv.setFillColor(WHITE)
#     canv.circle(left[0], left[1], size * 0.24, stroke=0, fill=1)
#     canv.circle(right[0], right[1], size * 0.24, stroke=0, fill=1)

#     canv.restoreState()


# def add_header_footer(canv, doc):
#     canv.saveState()
#     w, h = A4

#     # Top bar
#     canv.setFillColor(BLUE_DARK)
#     canv.rect(0, h - 22, w, 22, stroke=0, fill=1)

#     draw_chiefai_logo(canv, MARGIN + 6, h - 11, size=7)

#     canv.setFont("Helvetica-Bold", 8)
#     canv.setFillColor(WHITE)
#     canv.drawString(MARGIN + 16, h - 14, "ChiefAI  \u2022  Startup Intelligence Report")
#     canv.drawRightString(w - MARGIN, h - 14, "Powered by Microsoft Azure AI Foundry")

#     # Bottom bar
#     canv.setFillColor(GRAY_BG)
#     canv.rect(0, 0, w, 18, stroke=0, fill=1)
#     canv.setFillColor(GRAY_TEXT)
#     canv.setFont("Helvetica", 7.5)
#     canv.drawString(MARGIN, 6, "Generated by ChiefAI \u2014 AI Startup Intelligence Platform")
#     canv.drawRightString(w - MARGIN, 6, f"Page {canv.getPageNumber()}")

#     # Accent line under top bar
#     canv.setStrokeColor(TEAL)
#     canv.setLineWidth(1.5)
#     canv.line(0, h - 23, w, h - 23)

#     canv.restoreState()


# # ── Main Export Function ───────────────────────────────────────────────────────

# def export_report_pdf(report_id) -> str:
#     # ── Fetch data ──────────────────────────────────────────────────────────
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM startup_reports WHERE id=?", (report_id,))
#     report = cursor.fetchone()
#     conn.close()

#     if not report:
#         raise Exception(f"Report {report_id} not found")

#     data = json.loads(report["report_json"])

#     market   = data.get("market", {})
#     business = data.get("business", {})
#     investor = data.get("investor", {})
#     swot     = data.get("swot", {})
#     metadata = data.get("metadata", {})
#     exec_summary = data.get("executive_summary", {})
#     analysis_summary = data.get("analysis_summary", {})

#     # ── Derived values (matching dashboard UI) ───────────────────────────────
#     overall_score = analysis_summary.get("overall_score", 0) or 0
#     try:
#         overall_score = float(overall_score)
#     except (TypeError, ValueError):
#         overall_score = 0.0

#     outlook    = analysis_summary.get("investment_outlook", "N/A")
#     risk_level = analysis_summary.get("risk_level") or investor.get("investment_risk", "N/A")

#     readiness_raw = investor.get("readiness_score", 0)
#     try:
#         readiness_num = float(readiness_raw)
#     except (TypeError, ValueError):
#         readiness_num = 0.0

#     raise_amount = investor.get("recommended_raise") or investor.get("raise_amount", "N/A")
#     decision_text, decision_color = decision_from_score(overall_score)

#     # ── Styles & document setup ──────────────────────────────────────────────
#     S = build_styles()

#     filename = f"chiefai_report_{report_id}.pdf"
#     pdf = SimpleDocTemplate(
#         filename,
#         pagesize=A4,
#         leftMargin=MARGIN, rightMargin=MARGIN,
#         topMargin=30 * mm, bottomMargin=20 * mm,
#         title=f"ChiefAI Startup Report #{report_id}",
#         author="ChiefAI",
#         subject="AI Startup Intelligence Report",
#     )

#     C = []

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 1 — COVER / SCORECARD
#     # ══════════════════════════════════════════════════════════════════════════

#     # Title banner
#     cover_title = Table(
#         [[Paragraph("ChiefAI", S["ChiefTitle"])]],
#         colWidths=[PAGE_W - 2 * MARGIN],
#     )
#     cover_title.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
#         ("TOPPADDING",    (0, 0), (-1, -1), 20),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 16),
#     ]))
#     C.append(cover_title)

#     cover_sub = Table(
#         [[Paragraph("AI Startup Intelligence Report", S["ChiefSubtitle"])]],
#         colWidths=[PAGE_W - 2 * MARGIN],
#     )
#     cover_sub.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
#         ("TOPPADDING",    (0, 0), (-1, -1), 0),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 16),
#     ]))
#     C.append(cover_sub)

#     accent_strip = Table(
#         [[Paragraph("AI-Powered Startup Intelligence  \u2022  Powered by Microsoft Azure AI Foundry", S["CoverTag"])]],
#         colWidths=[PAGE_W - 2 * MARGIN],
#     )
#     accent_strip.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, -1), TEAL),
#         ("TOPPADDING",    (0, 0), (-1, -1), 5),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
#     ]))
#     C.append(accent_strip)
#     C.append(Spacer(1, 18))

#     # Score panel
#     sc = score_color(overall_score)
#     score_cell = [
#         Paragraph(f'<font color="#FFFFFF"><b>{int(overall_score)}</b></font>', S["CoverScore"]),
#         Paragraph('<font color="#C7E0F4">/ 100  Overall Score</font>', S["CoverScoreSub"]),
#         Spacer(1, 6),
#         Paragraph(f'<font color="#FFFFFF"><b>{outlook}</b></font>', ParagraphStyle(
#             "CoverOutlook", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE,
#             leading=16, alignment=TA_CENTER)),
#     ]
#     info_cell = [
#         Paragraph(f'<b>Report ID:</b>  #{report_id}', S["Body"]),
#         Spacer(1, 4),
#         Paragraph(f'<b>Generated:</b>  {fmt_dt(metadata.get("generated_at"))}', S["Body"]),
#         Spacer(1, 4),
#         Paragraph(f'<b>Funding Stage:</b>  {v(investor, "funding_stage")}', S["Body"]),
#         Spacer(1, 4),
#         Paragraph(f'<b>Recommended Raise:</b>  {v({"r": raise_amount}, "r")}', S["Body"]),
#         Spacer(1, 4),
#         Paragraph(f'<b>Investment Readiness:</b>  {readiness_raw} / 10', S["Body"]),
#         Spacer(1, 12),
#         Paragraph(
#             '<font color="#005A9E"><b>Powered by Microsoft Azure AI Foundry</b><br/>'
#             'Multi-Agent AI Orchestration for Startup Intelligence</font>',
#             S["BodySmall"]),
#     ]

#     cover_panel = Table(
#         [[score_cell, info_cell]],
#         colWidths=[(PAGE_W - 2 * MARGIN) * 0.42, (PAGE_W - 2 * MARGIN) * 0.58],
#     )
#     cover_panel.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), sc),
#         ("BACKGROUND",    (1, 0), (1, 0), GRAY_BG),
#         ("TOPPADDING",    (0, 0), (-1, -1), 18),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 18),
#         ("RIGHTPADDING",  (0, 0), (-1, -1), 18),
#         ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#     ]))
#     C.append(cover_panel)
#     C.append(Spacer(1, 16))

#     # KPI strip
#     kpi_data = [
#         [
#             Paragraph("<b>Market Size</b>", S["KpiLabel"]),
#             Paragraph("<b>Growth Rate</b>", S["KpiLabel"]),
#             Paragraph("<b>Funding Stage</b>", S["KpiLabel"]),
#             Paragraph("<b>Recommended Raise</b>", S["KpiLabel"]),
#         ],
#         [
#             Paragraph(v(market, "market_size"), S["KpiValue"]),
#             Paragraph(v(market, "growth_rate"), S["KpiValue"]),
#             Paragraph(v(investor, "funding_stage"), S["KpiValue"]),
#             Paragraph(v({"r": raise_amount}, "r"), S["KpiValue"]),
#         ],
#         [
#             Paragraph("Total Addressable Market", S["BodySmall"]),
#             Paragraph("CAGR", S["BodySmall"]),
#             Paragraph("AI Recommended Stage", S["BodySmall"]),
#             Paragraph("Target Capital", S["BodySmall"]),
#         ],
#     ]
#     kpi_w = (PAGE_W - 2 * MARGIN) / 4
#     kpi_strip = Table(kpi_data, colWidths=[kpi_w] * 4)
#     kpi_strip.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, -1), WHITE),
#         ("LINEABOVE",     (0, 0), (0, 0), 4, BLUE),
#         ("LINEABOVE",     (1, 0), (1, 0), 4, GREEN),
#         ("LINEABOVE",     (2, 0), (2, 0), 4, PURPLE),
#         ("LINEABOVE",     (3, 0), (3, 0), 4, ORANGE),
#         ("LINEAFTER",     (0, 0), (2, -1), 0.4, GRAY_BORDER),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
#         ("TOPPADDING",    (0, 0), (-1, -1), 8),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
#         ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
#     ]))
#     C.append(kpi_strip)
#     C.append(Spacer(1, 16))

#     # AI Investment Decision banner
#     decision_table = Table(
#         [[
#             Paragraph(f'<font color="#FFFFFF"><b>AI INVESTMENT DECISION:  {decision_text}</b></font>',
#                       ParagraphStyle("Decision", fontName="Helvetica-Bold", fontSize=11,
#                                      textColor=WHITE, leading=15, alignment=TA_CENTER)),
#             Paragraph(f'<font color="#FFFFFF">Risk:  <b>{str(risk_level).upper()}</b></font>',
#                       ParagraphStyle("RiskTag", fontName="Helvetica-Bold", fontSize=9,
#                                      textColor=WHITE, leading=13, alignment=TA_CENTER)),
#         ]],
#         colWidths=[(PAGE_W - 2 * MARGIN) * 0.72, (PAGE_W - 2 * MARGIN) * 0.28],
#     )
#     decision_table.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), decision_color),
#         ("BACKGROUND",    (1, 0), (1, 0), risk_color(risk_level)),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 12),
#         ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
#     ]))
#     C.append(decision_table)
#     C.append(PageBreak())

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 2 — EXECUTIVE SUMMARY
#     # ══════════════════════════════════════════════════════════════════════════

#     C += section_title("Executive Summary", "\u2139", S)

#     summary_text = exec_summary.get("executive_summary") or (
#         f'This startup operates in a market of <b>{v(market, "market_size")}</b> '
#         f'with a projected growth rate of <b>{v(market, "growth_rate")}</b>. '
#         f'The recommended funding stage is <b>{v(investor, "funding_stage")}</b> '
#         f'with a target raise of <b>{v({"r": raise_amount}, "r")}</b>.'
#     )
#     C.append(Paragraph(summary_text, S["Body"]))
#     C.append(Spacer(1, 10))

#     overview_rows = [
#         [Paragraph("<b>Field</b>", S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
#         [Paragraph("Business Model",  S["Body"]), Paragraph(v(exec_summary, "business_model"), S["Body"])],
#         [Paragraph("Target Customer", S["Body"]), Paragraph(v(exec_summary, "target_customer"), S["Body"])],
#         [Paragraph("Market Size",     S["Body"]), Paragraph(v(market, "market_size"), S["Body"])],
#         [Paragraph("Growth Rate",     S["Body"]), Paragraph(v(market, "growth_rate"), S["Body"])],
#         [Paragraph("Investment Readiness", S["Body"]), Paragraph(f"{readiness_raw} / 10", S["Body"])],
#         [Paragraph("Competitors", S["Body"]), Paragraph(
#             ", ".join([c.get("name", "-") if isinstance(c, dict) else str(c)
#                        for c in market.get("competitors", [])]) or "None identified",
#             S["Body"])],
#     ]
#     overview_t = Table(overview_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
#     overview_t.setStyle(two_col_detail_style())
#     C.append(overview_t)
#     C.append(Spacer(1, 16))

#     # ── AI Insights: Strengths / Risks / Opportunities (from SWOT) ───────────
#     C += section_title("AI Insights", "\u2726", S)

#     col3 = (PAGE_W - 2 * MARGIN) / 3
#     insights_t = Table([[
#         list_cell("STRENGTHS",          swot.get("strengths", []),     GREEN,  S),
#         list_cell("MAJOR RISKS",        swot.get("threats", []),       RED,    S),
#         list_cell("GROWTH OPPORTUNITIES", swot.get("opportunities", []), BLUE, S),
#     ]], colWidths=[col3, col3, col3])
#     insights_t.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
#         ("BACKGROUND",    (1, 0), (1, 0), RED_LIGHT),
#         ("BACKGROUND",    (2, 0), (2, 0), BLUE_LIGHT),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (1, -1), 0.4, GRAY_BORDER),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 10),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ]))
#     C.append(insights_t)
#     C.append(PageBreak())

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 3 — MARKET ANALYSIS
#     # ══════════════════════════════════════════════════════════════════════════

#     C += section_title("Market Analysis", "\u2316", S)

#     mkt_rows = [
#         [Paragraph("<b>Metric</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])],
#         [Paragraph("Market Size", S["Body"]), Paragraph(v(market, "market_size"), S["Body"])],
#         [Paragraph("Growth Rate (CAGR)", S["Body"]), Paragraph(v(market, "growth_rate"), S["Body"])],
#         [Paragraph("TAM", S["Body"]), Paragraph(v(market, "tam"), S["Body"])],
#         [Paragraph("SAM", S["Body"]), Paragraph(v(market, "sam"), S["Body"])],
#         [Paragraph("SOM", S["Body"]), Paragraph(v(market, "som"), S["Body"])],
#     ]
#     mkt_t = Table(mkt_rows, colWidths=[160, PAGE_W - 2 * MARGIN - 160])
#     mkt_t.setStyle(std_table_style())
#     C.append(mkt_t)
#     C.append(Spacer(1, 10))

#     # TAM/SAM/SOM explanations
#     for (label, key) in [
#         ("Total Addressable Market (TAM)", "tam_explanation"),
#         ("Serviceable Available Market (SAM)", "sam_explanation"),
#         ("Serviceable Obtainable Market (SOM)", "som_explanation"),
#     ]:
#         txt = market.get(key)
#         if txt:
#             C.append(Paragraph(f'<b><font color="#0078D4">{label}:</font></b>  {txt}', S["Body"]))
#             C.append(Spacer(1, 4))
#     C.append(Spacer(1, 8))

#     # Market Trends / Opportunities / Risks
#     trends_t = Table([[
#         list_cell("MARKET TRENDS",  market.get("market_trends", []),  BLUE,  S),
#         list_cell("OPPORTUNITIES",  market.get("opportunities", []),  GREEN, S),
#         list_cell("RISKS",          market.get("risks", []),          RED,   S),
#     ]], colWidths=[col3, col3, col3])
#     trends_t.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), BLUE_LIGHT),
#         ("BACKGROUND",    (1, 0), (1, 0), GREEN_LIGHT),
#         ("BACKGROUND",    (2, 0), (2, 0), RED_LIGHT),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (1, -1), 0.4, GRAY_BORDER),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 10),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ]))
#     C.append(trends_t)
#     C.append(Spacer(1, 14))

#     # Competitor Landscape
#     C += section_title("Competitor Landscape", "\u26A0", S)
#     competitors = market.get("competitors", [])
#     C.append(Paragraph(f"<b>{len(competitors)}</b> competitor(s) identified by AI.", S["Body"]))
#     C.append(Spacer(1, 6))
#     C.append(build_competitor_table(competitors, S))
#     C.append(PageBreak())

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 4 — SWOT SNAPSHOT
#     # ══════════════════════════════════════════════════════════════════════════

#     C += section_title("SWOT Snapshot", "\u25A6", S)
#     C.append(Paragraph(
#         "Strategic overview of internal strengths and weaknesses alongside "
#         "external opportunities and threats.", S["Body"]))
#     C.append(Spacer(1, 8))
#     C.append(build_swot_table(swot, S))
#     C.append(PageBreak())

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 5 — BUSINESS STRATEGY
#     # ══════════════════════════════════════════════════════════════════════════

#     C += section_title("Business Strategy", "\u2630", S)

#     biz_rows = [
#         [Paragraph("<b>Field</b>", S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
#         [Paragraph("Business Model",      S["Body"]), Paragraph(v(business, "business_model"), S["Body"])],
#         [Paragraph("Startup Vision",      S["Body"]), Paragraph(v(business, "startup_vision"), S["Body"])],
#         [Paragraph("Mission Statement",   S["Body"]), Paragraph(v(business, "mission_statement"), S["Body"])],
#         [Paragraph("Value Proposition",   S["Body"]), Paragraph(v(business, "value_proposition"), S["Body"])],
#         [Paragraph("USP",                 S["Body"]), Paragraph(v(business, "usp"), S["Body"])],
#         [Paragraph("Target Customer",     S["Body"]), Paragraph(v(business, "target_customer"), S["Body"])],
#         [Paragraph("Pricing Strategy",    S["Body"]), Paragraph(v(business, "pricing_strategy"), S["Body"])],
#         [Paragraph("Revenue Model",       S["Body"]), Paragraph(v(business, "revenue_model"), S["Body"])],
#         [Paragraph("Monetization Strategy", S["Body"]), Paragraph(v(business, "monetization_strategy"), S["Body"])],
#         [Paragraph("Expected Revenue Growth", S["Body"]), Paragraph(v(business, "expected_revenue_growth"), S["Body"])],
#         [Paragraph("Go-To-Market Strategy", S["Body"]), Paragraph(v(business, "go_to_market"), S["Body"])],
#         [Paragraph("Sales Strategy",      S["Body"]), Paragraph(v(business, "sales_strategy"), S["Body"])],
#         [Paragraph("Partnership Strategy", S["Body"]), Paragraph(v(business, "partnership_strategy"), S["Body"])],
#         [Paragraph("Expansion Strategy",  S["Body"]), Paragraph(v(business, "expansion_strategy"), S["Body"])],
#         [Paragraph("Scaling Plan",        S["Body"]), Paragraph(v(business, "scaling_plan"), S["Body"])],
#         [Paragraph("Market Expansion",    S["Body"]), Paragraph(v(business, "market_expansion"), S["Body"])],
#         [Paragraph("Innovation Strategy", S["Body"]), Paragraph(v(business, "innovation_strategy"), S["Body"])],
#         [Paragraph("AI Advantage",        S["Body"]), Paragraph(v(business, "ai_advantage"), S["Body"])],
#         [Paragraph("Technology Advantage", S["Body"]), Paragraph(v(business, "technology_advantage"), S["Body"])],
#     ]
#     biz_t = Table(biz_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
#     biz_t.setStyle(two_col_detail_style())
#     C.append(biz_t)
#     C.append(Spacer(1, 14))

#     # Revenue Streams / Customer Segments / Channels
#     col2 = (PAGE_W - 2 * MARGIN) / 2
#     business_lists_t = Table([
#         [list_cell("REVENUE STREAMS",      business.get("revenue_streams", []),      GREEN, S),
#          list_cell("CUSTOMER SEGMENTS",    business.get("customer_segments", []),    BLUE,  S)],
#         [list_cell("CUSTOMER PAIN POINTS", business.get("customer_pain_points", []), RED,   S),
#          list_cell("KEY ADVANTAGES",       business.get("key_advantages", []),       PURPLE, S)],
#         [list_cell("MARKETING CHANNELS",   business.get("marketing_channels", []),   BLUE,  S),
#          list_cell("DISTRIBUTION CHANNELS", business.get("distribution_channels", []), GREEN, S)],
#         [list_cell("GROWTH ROADMAP",       business.get("growth_roadmap", []),       ORANGE, S),
#          list_cell("COMPETITIVE DIFFERENTIATORS", business.get("competitive_differentiators", []), TEAL, S)],
#     ], colWidths=[col2, col2])
#     business_lists_t.setStyle(TableStyle([
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
#         ("LINEBELOW",     (0, 0), (-1, -2), 0.4, GRAY_BORDER),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 10),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ]))
#     C.append(business_lists_t)
#     C.append(PageBreak())

#     # ══════════════════════════════════════════════════════════════════════════
#     # PAGE 6 — INVESTOR READINESS
#     # ══════════════════════════════════════════════════════════════════════════

#     C += section_title("Investor Readiness", "\u25CE", S)

#     inv_rows = [
#         [Paragraph("<b>Metric</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])],
#         [Paragraph("Overall Score", S["Body"]),
#          Paragraph(f'<b><font color="#{score_color(overall_score).hexval()[2:]}">{int(overall_score)}/100</font></b>', S["Body"])],
#         [Paragraph("Investment Readiness", S["Body"]),
#          Paragraph(f'<b><font color="#{score_color(readiness_num * 10).hexval()[2:]}">{readiness_raw}/10</font></b>', S["Body"])],
#         [Paragraph("Investment Outlook", S["Body"]), Paragraph(v({"o": outlook}, "o"), S["Body"])],
#         [Paragraph("Funding Stage", S["Body"]), Paragraph(v(investor, "funding_stage"), S["Body"])],
#         [Paragraph("Recommended Raise", S["Body"]), Paragraph(v({"r": raise_amount}, "r"), S["Body"])],
#         [Paragraph("Investment Risk", S["Body"]),
#          Paragraph(f'<b><font color="#{risk_color(risk_level).hexval()[2:]}">{str(risk_level).upper()}</font></b>', S["Body"])],
#     ]
#     inv_t = Table(inv_rows, colWidths=[180, PAGE_W - 2 * MARGIN - 180])
#     inv_t.setStyle(two_col_detail_style())
#     C.append(inv_t)
#     C.append(Spacer(1, 14))

#     # Strengths & Weaknesses
#     sw_t = Table([[
#         list_cell("STRENGTHS",  investor.get("strengths", []),  GREEN,  S),
#         list_cell("WEAKNESSES", investor.get("weaknesses", []), ORANGE, S),
#     ]], colWidths=[col2, col2])
#     sw_t.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
#         ("BACKGROUND",    (1, 0), (1, 0), ORANGE_LIGHT),
#         ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
#         ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
#         ("TOPPADDING",    (0, 0), (-1, -1), 10),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
#         ("LEFTPADDING",   (0, 0), (-1, -1), 10),
#         ("VALIGN",        (0, 0), (-1, -1), "TOP"),
#     ]))
#     C.append(sw_t)
#     C.append(Spacer(1, 14))

#     # Investment Risks
#     C.append(Paragraph("Investment Risks", S["SubHeader"]))
#     C += bullet_list(investor.get("risks", []), S["BodySmall"])
#     C.append(Spacer(1, 10))

#     # AI Recommendations
#     C.append(Paragraph("AI Recommendations", S["SubHeader"]))
#     recs = investor.get("recommendations", [])
#     if recs:
#         for i, rec in enumerate(recs, 1):
#             C.append(Paragraph(f'<b><font color="#0078D4">{i}.</font></b>  {rec}', S["Body"]))
#             C.append(Spacer(1, 3))
#     else:
#         C.append(Paragraph("No AI recommendations available.", S["BodySmall"]))

#     C.append(Spacer(1, 20))

#     # ── Final Disclaimer ─────────────────────────────────────────────────────
#     disclaimer = Table([[
#         Paragraph(
#             '<b>Generated by ChiefAI \u2014 AI Startup Intelligence Platform</b>  \u2022  '
#             'Powered by Microsoft Azure AI Foundry  \u2022  '
#             'Confidential \u2022 For Evaluation Purposes Only',
#             ParagraphStyle("Disc", fontName="Helvetica", fontSize=7.5,
#                            textColor=GRAY_TEXT, leading=11, alignment=TA_CENTER)),
#     ]], colWidths=[PAGE_W - 2 * MARGIN])
#     disclaimer.setStyle(TableStyle([
#         ("BACKGROUND",    (0, 0), (-1, -1), GRAY_BG),
#         ("TOPPADDING",    (0, 0), (-1, -1), 8),
#         ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
#         ("BOX",           (0, 0), (-1, -1), 0.4, GRAY_BORDER),
#     ]))
#     C.append(disclaimer)

#     # ── Build ────────────────────────────────────────────────────────────────
#     pdf.build(
#         C,
#         onFirstPage=add_header_footer,
#         onLaterPages=add_header_footer,
#     )

#     return filename

# Fixed Code

"""
ChiefAI — Startup Intelligence Platform
PDF Export Service

Generates a polished, judge-ready PDF report containing only the
information that is shown in the ChiefAI dashboard UI:
  - Cover / scorecard (overall score, outlook, risk, funding stage, raise)
  - Executive Summary
  - Market Analysis (size, growth, TAM/SAM/SOM, competitors, trends,
    opportunities, risks)
  - SWOT Snapshot
  - Business Strategy
  - Investor Readiness (readiness score, strengths, weaknesses, risks,
    recommendations)

No internal AI-agent execution metadata (agent names, execution times,
agent counts) is included, matching the public-facing dashboard.
"""

import json
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

from app.database.db import get_connection


# ── Brand Palette (Fluent-inspired) ────────────────────────────────────────────

BLUE         = colors.HexColor("#0078D4")
BLUE_DARK    = colors.HexColor("#005A9E")
BLUE_LIGHT   = colors.HexColor("#E5F1FB")
TEAL         = colors.HexColor("#50E6FF")
PURPLE       = colors.HexColor("#8764B8")
GREEN        = colors.HexColor("#107C10")
GREEN_LIGHT  = colors.HexColor("#DFF6DD")
ORANGE       = colors.HexColor("#FF8C00")
ORANGE_LIGHT = colors.HexColor("#FFF4CE")
RED          = colors.HexColor("#D13438")
RED_LIGHT    = colors.HexColor("#FDE7E9")
GRAY_TEXT    = colors.HexColor("#605E5C")
GRAY_DARK    = colors.HexColor("#323130")
GRAY_BG      = colors.HexColor("#F3F2F1")
GRAY_BORDER  = colors.HexColor("#E1DFDD")
WHITE        = colors.white

PAGE_W, PAGE_H = A4
MARGIN = 18 * mm


# ── Style Builder ──────────────────────────────────────────────────────────────

def build_styles():
    styles = getSampleStyleSheet()

    def add(name, **kw):
        styles.add(ParagraphStyle(name=name, **kw))

    add("ChiefTitle",
        fontName="Helvetica-Bold", fontSize=28, textColor=WHITE,
        leading=34, spaceAfter=2, alignment=TA_LEFT)

    add("ChiefSubtitle",
        fontName="Helvetica", fontSize=12, textColor=colors.HexColor("#C7E0F4"),
        leading=16, spaceAfter=0, alignment=TA_LEFT)

    add("SectionHeader",
        fontName="Helvetica-Bold", fontSize=14, textColor=BLUE_DARK,
        leading=18, spaceBefore=14, spaceAfter=6, alignment=TA_LEFT)

    add("SubHeader",
        fontName="Helvetica-Bold", fontSize=10.5, textColor=GRAY_DARK,
        leading=14, spaceBefore=6, spaceAfter=3, alignment=TA_LEFT)

    add("Body",
        fontName="Helvetica", fontSize=9.5, textColor=GRAY_DARK,
        leading=14, spaceAfter=3, alignment=TA_LEFT)

    add("BodySmall",
        fontName="Helvetica", fontSize=8.5, textColor=GRAY_TEXT,
        leading=12, spaceAfter=2, alignment=TA_LEFT)

    add("KpiValue",
        fontName="Helvetica-Bold", fontSize=22, textColor=GRAY_DARK,
        leading=26, spaceAfter=2, alignment=TA_CENTER)

    add("KpiLabel",
        fontName="Helvetica-Bold", fontSize=7.5, textColor=GRAY_TEXT,
        leading=10, spaceAfter=0, alignment=TA_CENTER)

    add("CoverScore",
        fontName="Helvetica-Bold", fontSize=46, textColor=WHITE,
        leading=52, alignment=TA_CENTER)

    add("CoverScoreSub",
        fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#C7E0F4"),
        leading=14, alignment=TA_CENTER)

    add("CoverTag",
        fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
        leading=11, spaceAfter=0, alignment=TA_CENTER)

    return styles


# ── Table Style Factories ───────────────────────────────────────────────────────

def std_table_style(header_bg=BLUE, alt_row=BLUE_LIGHT):
    return TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 9),
        ("TOPPADDING",    (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 9),
        ("ALIGN",         (0, 0), (-1, 0), "LEFT"),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("TOPPADDING",    (0, 1), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 7),
        ("TEXTCOLOR",     (0, 1), (-1, -1), GRAY_DARK),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, alt_row]),
        ("LINEBELOW",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
    ])


def two_col_detail_style():
    return TableStyle([
        ("BACKGROUND",    (0, 0), (0, -1), GRAY_BG),
        ("FONTNAME",      (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("TEXTCOLOR",     (0, 0), (0, -1), BLUE_DARK),
        ("TEXTCOLOR",     (1, 0), (1, -1), GRAY_DARK),
        ("FONTNAME",      (1, 0), (1, -1), "Helvetica"),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ])


# ── Helpers ───────────────────────────────────────────────────────────────────

def v(d: dict, key: str, default="Not available") -> str:
    val = d.get(key, default)
    if val is None or val == "":
        return default
    return str(val)


def fmt_dt(s) -> str:
    if not s:
        return "-"
    try:
        return datetime.fromisoformat(str(s)).strftime("%B %d, %Y  %H:%M")
    except Exception:
        return str(s)


def score_color(n: float):
    if n >= 75: return GREEN
    if n >= 50: return ORANGE
    return RED


def risk_color(risk: str):
    r = (risk or "").lower()
    if "low" in r: return GREEN
    if "medium" in r or "moderate" in r: return ORANGE
    if "high" in r: return RED
    return GRAY_TEXT


def decision_from_score(score: float):
    if score >= 75: return ("STRONG INVEST", GREEN)
    if score >= 50: return ("CONSIDER INVEST", ORANGE)
    return ("NEEDS IMPROVEMENT", RED)


def section_title(title: str, icon: str, styles) -> list:
    return [
        HRFlowable(width="100%", thickness=0.5, color=GRAY_BORDER, spaceAfter=6),
        Paragraph(f'<font color="#0078D4">\u25A0</font>  {title}', styles["SectionHeader"]),
        Spacer(1, 4),
    ]


def bullet_list(items, style, prefix="  \u2022  ") -> list:
    if not items:
        return [Paragraph(f"{prefix}No data available.", style)]
    return [Paragraph(f"{prefix}{item}", style) for item in items]


def list_cell(title, items, fg, styles):
    lines = [Paragraph(f'<b><font color="#{fg.hexval()[2:]}">{title}</font></b>', styles["SubHeader"])]
    if items:
        for it in items:
            lines.append(Paragraph(f'  \u2022  {it}', styles["BodySmall"]))
    else:
        lines.append(Paragraph("  \u2022  No data available.", styles["BodySmall"]))
    return lines


# ── SWOT 2x2 ──────────────────────────────────────────────────────────────────

def build_swot_table(swot: dict, styles) -> Table:
    s_items  = swot.get("strengths", [])
    w_items  = swot.get("weaknesses", [])
    o_items  = swot.get("opportunities", [])
    t_items  = swot.get("threats", [])

    col_w = (PAGE_W - 2 * MARGIN) / 2

    t = Table([
        [list_cell("STRENGTHS", s_items, GREEN, styles), list_cell("WEAKNESSES", w_items, RED, styles)],
        [list_cell("OPPORTUNITIES", o_items, BLUE, styles), list_cell("THREATS", t_items, ORANGE, styles)],
    ], colWidths=[col_w, col_w])

    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), RED_LIGHT),
        ("BACKGROUND",    (0, 1), (0, 1), BLUE_LIGHT),
        ("BACKGROUND",    (1, 1), (1, 1), ORANGE_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (0, -1), 0.6, GRAY_BORDER),
        ("LINEBELOW",     (0, 0), (-1, 0), 0.6, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    return t


# ── Competitor Table ──────────────────────────────────────────────────────────

def build_competitor_table(competitors: list, styles):
    if not competitors:
        return Paragraph("No competitors identified.", styles["BodySmall"])

    rows = [[
        Paragraph("<b>#</b>", styles["Body"]),
        Paragraph("<b>Competitor</b>", styles["Body"]),
        Paragraph("<b>Key Strength</b>", styles["Body"]),
    ]]
    for i, c in enumerate(competitors, start=1):
        if isinstance(c, dict):
            name     = c.get("name", "-")
            strength = c.get("strength", "-")
        else:
            name, strength = str(c), "-"
        rows.append([
            Paragraph(str(i), styles["Body"]),
            Paragraph(f'<b><font color="#0078D4">{name}</font></b>', styles["Body"]),
            Paragraph(strength, styles["BodySmall"]),
        ])

    t = Table(rows, colWidths=[25, 160, PAGE_W - 2 * MARGIN - 185])
    t.setStyle(std_table_style())
    return t


# ── Header / Footer (drawn on every page, with ChiefAI logo) ──────────────────

def draw_chiefai_logo(canv, x, y, size=9):
    """Draw the ChiefAI multi-agent network mark (matches the app logo)."""
    canv.saveState()

    # Connection lines
    canv.setStrokeColor(colors.HexColor("#7FD6FF"))
    canv.setLineWidth(0.8)
    top    = (x, y + size)
    left   = (x - size * 0.85, y - size * 0.55)
    right  = (x + size * 0.85, y - size * 0.55)
    canv.line(top[0], top[1], left[0], left[1])
    canv.line(top[0], top[1], right[0], right[1])
    canv.line(left[0], left[1], right[0], right[1])

    # Nodes
    canv.setFillColor(BLUE)
    canv.circle(top[0], top[1], size * 0.32, stroke=0, fill=1)
    canv.setFillColor(WHITE)
    canv.circle(left[0], left[1], size * 0.24, stroke=0, fill=1)
    canv.circle(right[0], right[1], size * 0.24, stroke=0, fill=1)

    canv.restoreState()


def add_header_footer(canv, doc):
    canv.saveState()
    w, h = A4

    # Top bar
    canv.setFillColor(BLUE_DARK)
    canv.rect(0, h - 22, w, 22, stroke=0, fill=1)

    draw_chiefai_logo(canv, MARGIN + 6, h - 11, size=7)

    canv.setFont("Helvetica-Bold", 8)
    canv.setFillColor(WHITE)
    canv.drawString(MARGIN + 16, h - 14, "ChiefAI  \u2022  Startup Intelligence Report")
    canv.drawRightString(w - MARGIN, h - 14, "Powered by Microsoft Azure AI Foundry")

    # Bottom bar
    canv.setFillColor(GRAY_BG)
    canv.rect(0, 0, w, 18, stroke=0, fill=1)
    canv.setFillColor(GRAY_TEXT)
    canv.setFont("Helvetica", 7.5)
    canv.drawString(MARGIN, 6, "Generated by ChiefAI \u2014 AI Startup Intelligence Platform")
    canv.drawRightString(w - MARGIN, 6, f"Page {canv.getPageNumber()}")

    # Accent line under top bar
    canv.setStrokeColor(TEAL)
    canv.setLineWidth(1.5)
    canv.line(0, h - 23, w, h - 23)

    canv.restoreState()


# ── Main Export Function ───────────────────────────────────────────────────────

def export_report_pdf(report_id) -> str:
    # ── Fetch data ──────────────────────────────────────────────────────────
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM startup_reports WHERE id=?", (report_id,))
    report = cursor.fetchone()
    conn.close()

    if not report:
        raise Exception(f"Report {report_id} not found")

    data = json.loads(report["report_json"])

    market   = data.get("market", {})
    business = data.get("business", {})
    investor = data.get("investor", {})
    swot     = data.get("swot", {})
    metadata = data.get("metadata", {})
    exec_summary = data.get("executive_summary", {})
    analysis_summary = data.get("analysis_summary", {})

    # ── Derived values (matching dashboard UI) ───────────────────────────────
    overall_score = analysis_summary.get("overall_score", 0) or 0
    try:
        overall_score = float(overall_score)
    except (TypeError, ValueError):
        overall_score = 0.0

    outlook    = analysis_summary.get("investment_outlook", "N/A")
    risk_level = analysis_summary.get("risk_level") or investor.get("investment_risk", "N/A")

    readiness_raw = investor.get("readiness_score", 0)
    try:
        readiness_num = float(readiness_raw)
    except (TypeError, ValueError):
        readiness_num = 0.0

    raise_amount = investor.get("recommended_raise") or investor.get("raise_amount", "N/A")
    decision_text, decision_color = decision_from_score(overall_score)

    # ── Styles & document setup ──────────────────────────────────────────────
    S = build_styles()

    filename = f"chiefai_report_{report_id}.pdf"
    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=30 * mm, bottomMargin=20 * mm,
        title=f"ChiefAI Startup Report #{report_id}",
        author="ChiefAI",
        subject="AI Startup Intelligence Report",
    )

    C = []

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 1 — COVER / SCORECARD
    # ══════════════════════════════════════════════════════════════════════════

    # Title banner
    cover_title = Table(
        [[Paragraph("ChiefAI", S["ChiefTitle"])]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    cover_title.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 20),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 16),
    ]))
    C.append(cover_title)

    cover_sub = Table(
        [[Paragraph("AI Startup Intelligence Report", S["ChiefSubtitle"])]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    cover_sub.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING",   (0, 0), (-1, -1), 16),
    ]))
    C.append(cover_sub)

    accent_strip = Table(
        [[Paragraph("AI-Powered Startup Intelligence  \u2022  Powered by Microsoft Azure AI Foundry", S["CoverTag"])]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    accent_strip.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), TEAL),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    C.append(accent_strip)
    C.append(Spacer(1, 18))

    # Score panel
    sc = score_color(overall_score)
    score_cell = [
        Paragraph(f'<font color="#FFFFFF"><b>{int(overall_score)}</b></font>', S["CoverScore"]),
        Paragraph('<font color="#C7E0F4">/ 100  Overall Score</font>', S["CoverScoreSub"]),
        Spacer(1, 6),
        Paragraph(f'<font color="#FFFFFF"><b>{outlook}</b></font>', ParagraphStyle(
            "CoverOutlook", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE,
            leading=16, alignment=TA_CENTER)),
    ]
    info_cell = [
        Paragraph(f'<b>Report ID:</b>  #{report_id}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Generated:</b>  {fmt_dt(metadata.get("generated_at"))}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Funding Stage:</b>  {v(investor, "funding_stage")}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Recommended Raise:</b>  {v({"r": raise_amount}, "r")}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Investment Readiness:</b>  {readiness_raw} / 10', S["Body"]),
        Spacer(1, 12),
        Paragraph(
            '<font color="#005A9E"><b>Powered by Microsoft Azure AI Foundry</b><br/>'
            'Multi-Agent AI Orchestration for Startup Intelligence</font>',
            S["BodySmall"]),
    ]

    cover_panel = Table(
        [[score_cell, info_cell]],
        colWidths=[(PAGE_W - 2 * MARGIN) * 0.42, (PAGE_W - 2 * MARGIN) * 0.58],
    )
    cover_panel.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), sc),
        ("BACKGROUND",    (1, 0), (1, 0), GRAY_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 18),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 18),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
    ]))
    C.append(cover_panel)
    C.append(Spacer(1, 16))

    # KPI strip
    kpi_data = [
        [
            Paragraph("<b>Market Size</b>", S["KpiLabel"]),
            Paragraph("<b>Growth Rate</b>", S["KpiLabel"]),
            Paragraph("<b>Funding Stage</b>", S["KpiLabel"]),
            Paragraph("<b>Recommended Raise</b>", S["KpiLabel"]),
        ],
        [
            Paragraph(v(market, "market_size"), S["KpiValue"]),
            Paragraph(v(market, "growth_rate"), S["KpiValue"]),
            Paragraph(v(investor, "funding_stage"), S["KpiValue"]),
            Paragraph(v({"r": raise_amount}, "r"), S["KpiValue"]),
        ],
        [
            Paragraph("Total Addressable Market", S["BodySmall"]),
            Paragraph("CAGR", S["BodySmall"]),
            Paragraph("AI Recommended Stage", S["BodySmall"]),
            Paragraph("Target Capital", S["BodySmall"]),
        ],
    ]
    kpi_w = (PAGE_W - 2 * MARGIN) / 4
    kpi_strip = Table(kpi_data, colWidths=[kpi_w] * 4)
    kpi_strip.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), WHITE),
        ("LINEABOVE",     (0, 0), (0, 0), 4, BLUE),
        ("LINEABOVE",     (1, 0), (1, 0), 4, GREEN),
        ("LINEABOVE",     (2, 0), (2, 0), 4, PURPLE),
        ("LINEABOVE",     (3, 0), (3, 0), 4, ORANGE),
        ("LINEAFTER",     (0, 0), (2, -1), 0.4, GRAY_BORDER),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    C.append(kpi_strip)
    C.append(Spacer(1, 16))

    # AI Investment Decision banner
    decision_table = Table(
        [[
            Paragraph(f'<font color="#FFFFFF"><b>AI INVESTMENT DECISION:  {decision_text}</b></font>',
                      ParagraphStyle("Decision", fontName="Helvetica-Bold", fontSize=11,
                                     textColor=WHITE, leading=15, alignment=TA_CENTER)),
            Paragraph(f'<font color="#FFFFFF">Risk:  <b>{str(risk_level).upper()}</b></font>',
                      ParagraphStyle("RiskTag", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=WHITE, leading=13, alignment=TA_CENTER)),
        ]],
        colWidths=[(PAGE_W - 2 * MARGIN) * 0.72, (PAGE_W - 2 * MARGIN) * 0.28],
    )
    decision_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), decision_color),
        ("BACKGROUND",    (1, 0), (1, 0), risk_color(risk_level)),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    C.append(decision_table)
    C.append(Spacer(1, 20))

    # Report contents index
    contents_items = [
        ("1", "Executive Summary & AI Insights"),
        ("2", "Market Analysis & Competitor Landscape"),
        ("3", "SWOT Snapshot"),
        ("4", "Business Strategy"),
        ("5", "Investor Readiness & AI Recommendations"),
    ]
    contents_rows = [[
        Paragraph("<b>What's Inside This Report</b>", ParagraphStyle(
            "ContentsHeader", fontName="Helvetica-Bold", fontSize=11,
            textColor=BLUE_DARK, leading=15)),
        Paragraph("", S["Body"]),
    ]]
    for num, label in contents_items:
        contents_rows.append([
            Paragraph(f'<font color="#0078D4"><b>{num}</b></font>', S["Body"]),
            Paragraph(label, S["Body"]),
        ])
    contents_t = Table(contents_rows, colWidths=[24, PAGE_W - 2 * MARGIN - 24])
    contents_t.setStyle(TableStyle([
        ("SPAN", (0, 0), (1, 0)),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING",    (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEBELOW",     (0, 0), (-1, 0), 0.6, GRAY_BORDER),
        ("LEFTPADDING",   (0, 0), (-1, -1), 14),
        ("TOPPADDING",    (0, 0), (-1, 0), 12),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    C.append(contents_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 2 — EXECUTIVE SUMMARY
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Executive Summary", "\u2139", S)

    summary_text = exec_summary.get("executive_summary") or (
        f'This startup operates in a market of <b>{v(market, "market_size")}</b> '
        f'with a projected growth rate of <b>{v(market, "growth_rate")}</b>. '
        f'The recommended funding stage is <b>{v(investor, "funding_stage")}</b> '
        f'with a target raise of <b>{v({"r": raise_amount}, "r")}</b>.'
    )
    C.append(Paragraph(summary_text, S["Body"]))
    C.append(Spacer(1, 10))

    overview_rows = [
        [Paragraph("<b>Field</b>", S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
        [Paragraph("Business Model",  S["Body"]), Paragraph(v(exec_summary, "business_model"), S["Body"])],
        [Paragraph("Target Customer", S["Body"]), Paragraph(v(exec_summary, "target_customer"), S["Body"])],
        [Paragraph("Market Size",     S["Body"]), Paragraph(v(market, "market_size"), S["Body"])],
        [Paragraph("Growth Rate",     S["Body"]), Paragraph(v(market, "growth_rate"), S["Body"])],
        [Paragraph("Investment Readiness", S["Body"]), Paragraph(f"{readiness_raw} / 10", S["Body"])],
        [Paragraph("Competitors", S["Body"]), Paragraph(
            ", ".join([c.get("name", "-") if isinstance(c, dict) else str(c)
                       for c in market.get("competitors", [])]) or "None identified",
            S["Body"])],
    ]
    overview_t = Table(overview_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
    overview_t.setStyle(two_col_detail_style())
    C.append(overview_t)
    C.append(Spacer(1, 16))

    # ── AI Insights: Strengths / Risks / Opportunities (from SWOT) ───────────
    C += section_title("AI Insights", "\u2726", S)

    col3 = (PAGE_W - 2 * MARGIN) / 3
    insights_t = Table([[
        list_cell("STRENGTHS",          swot.get("strengths", []),     GREEN,  S),
        list_cell("MAJOR RISKS",        swot.get("threats", []),       RED,    S),
        list_cell("GROWTH OPPORTUNITIES", swot.get("opportunities", []), BLUE, S),
    ]], colWidths=[col3, col3, col3])
    insights_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), RED_LIGHT),
        ("BACKGROUND",    (2, 0), (2, 0), BLUE_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (1, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(insights_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 3 — MARKET ANALYSIS
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Market Analysis", "\u2316", S)

    mkt_rows = [
        [Paragraph("<b>Metric</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])],
        [Paragraph("Market Size", S["Body"]), Paragraph(v(market, "market_size"), S["Body"])],
        [Paragraph("Growth Rate (CAGR)", S["Body"]), Paragraph(v(market, "growth_rate"), S["Body"])],
        [Paragraph("TAM", S["Body"]), Paragraph(v(market, "tam"), S["Body"])],
        [Paragraph("SAM", S["Body"]), Paragraph(v(market, "sam"), S["Body"])],
        [Paragraph("SOM", S["Body"]), Paragraph(v(market, "som"), S["Body"])],
    ]
    mkt_t = Table(mkt_rows, colWidths=[160, PAGE_W - 2 * MARGIN - 160])
    mkt_t.setStyle(std_table_style())
    C.append(mkt_t)
    C.append(Spacer(1, 10))

    # TAM/SAM/SOM explanations
    for (label, key) in [
        ("Total Addressable Market (TAM)", "tam_explanation"),
        ("Serviceable Available Market (SAM)", "sam_explanation"),
        ("Serviceable Obtainable Market (SOM)", "som_explanation"),
    ]:
        txt = market.get(key)
        if txt:
            C.append(Paragraph(f'<b><font color="#0078D4">{label}:</font></b>  {txt}', S["Body"]))
            C.append(Spacer(1, 4))
    C.append(Spacer(1, 8))

    # Market Trends / Opportunities / Risks
    trends_t = Table([[
        list_cell("MARKET TRENDS",  market.get("market_trends", []),  BLUE,  S),
        list_cell("OPPORTUNITIES",  market.get("opportunities", []),  GREEN, S),
        list_cell("RISKS",          market.get("risks", []),          RED,   S),
    ]], colWidths=[col3, col3, col3])
    trends_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), BLUE_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), GREEN_LIGHT),
        ("BACKGROUND",    (2, 0), (2, 0), RED_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (1, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(trends_t)
    C.append(Spacer(1, 14))

    # Competitor Landscape
    C += section_title("Competitor Landscape", "\u26A0", S)
    competitors = market.get("competitors", [])
    C.append(Paragraph(f"<b>{len(competitors)}</b> competitor(s) identified by AI.", S["Body"]))
    C.append(Spacer(1, 6))
    C.append(build_competitor_table(competitors, S))
    C.append(Spacer(1, 14))

    # ══════════════════════════════════════════════════════════════════════════
    # SWOT SNAPSHOT (continues on same flow — no forced page break)
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("SWOT Snapshot", "\u25A6", S)
    C.append(Paragraph(
        "Strategic overview of internal strengths and weaknesses alongside "
        "external opportunities and threats.", S["Body"]))
    C.append(Spacer(1, 8))
    C.append(build_swot_table(swot, S))
    C.append(Spacer(1, 16))

    # ══════════════════════════════════════════════════════════════════════════
    # BUSINESS STRATEGY (continues on same flow — no forced page break)
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Business Strategy", "\u2630", S)

    biz_rows = [
        [Paragraph("<b>Field</b>", S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
        [Paragraph("Business Model",      S["Body"]), Paragraph(v(business, "business_model"), S["Body"])],
        [Paragraph("Startup Vision",      S["Body"]), Paragraph(v(business, "startup_vision"), S["Body"])],
        [Paragraph("Mission Statement",   S["Body"]), Paragraph(v(business, "mission_statement"), S["Body"])],
        [Paragraph("Value Proposition",   S["Body"]), Paragraph(v(business, "value_proposition"), S["Body"])],
        [Paragraph("USP",                 S["Body"]), Paragraph(v(business, "usp"), S["Body"])],
        [Paragraph("Target Customer",     S["Body"]), Paragraph(v(business, "target_customer"), S["Body"])],
        [Paragraph("Pricing Strategy",    S["Body"]), Paragraph(v(business, "pricing_strategy"), S["Body"])],
        [Paragraph("Revenue Model",       S["Body"]), Paragraph(v(business, "revenue_model"), S["Body"])],
        [Paragraph("Monetization Strategy", S["Body"]), Paragraph(v(business, "monetization_strategy"), S["Body"])],
        [Paragraph("Expected Revenue Growth", S["Body"]), Paragraph(v(business, "expected_revenue_growth"), S["Body"])],
        [Paragraph("Go-To-Market Strategy", S["Body"]), Paragraph(v(business, "go_to_market"), S["Body"])],
        [Paragraph("Sales Strategy",      S["Body"]), Paragraph(v(business, "sales_strategy"), S["Body"])],
        [Paragraph("Partnership Strategy", S["Body"]), Paragraph(v(business, "partnership_strategy"), S["Body"])],
        [Paragraph("Expansion Strategy",  S["Body"]), Paragraph(v(business, "expansion_strategy"), S["Body"])],
        [Paragraph("Scaling Plan",        S["Body"]), Paragraph(v(business, "scaling_plan"), S["Body"])],
        [Paragraph("Market Expansion",    S["Body"]), Paragraph(v(business, "market_expansion"), S["Body"])],
        [Paragraph("Innovation Strategy", S["Body"]), Paragraph(v(business, "innovation_strategy"), S["Body"])],
        [Paragraph("AI Advantage",        S["Body"]), Paragraph(v(business, "ai_advantage"), S["Body"])],
        [Paragraph("Technology Advantage", S["Body"]), Paragraph(v(business, "technology_advantage"), S["Body"])],
    ]
    biz_t = Table(biz_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
    biz_t.setStyle(two_col_detail_style())
    C.append(biz_t)
    C.append(Spacer(1, 14))

    # Revenue Streams / Customer Segments / Channels
    col2 = (PAGE_W - 2 * MARGIN) / 2
    business_lists_t = Table([
        [list_cell("REVENUE STREAMS",      business.get("revenue_streams", []),      GREEN, S),
         list_cell("CUSTOMER SEGMENTS",    business.get("customer_segments", []),    BLUE,  S)],
        [list_cell("CUSTOMER PAIN POINTS", business.get("customer_pain_points", []), RED,   S),
         list_cell("KEY ADVANTAGES",       business.get("key_advantages", []),       PURPLE, S)],
        [list_cell("MARKETING CHANNELS",   business.get("marketing_channels", []),   BLUE,  S),
         list_cell("DISTRIBUTION CHANNELS", business.get("distribution_channels", []), GREEN, S)],
        [list_cell("GROWTH ROADMAP",       business.get("growth_roadmap", []),       ORANGE, S),
         list_cell("COMPETITIVE DIFFERENTIATORS", business.get("competitive_differentiators", []), TEAL, S)],
    ], colWidths=[col2, col2])
    business_lists_t.setStyle(TableStyle([
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
        ("LINEBELOW",     (0, 0), (-1, -2), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(business_lists_t)
    C.append(Spacer(1, 16))

    # ══════════════════════════════════════════════════════════════════════════
    # INVESTOR READINESS (continues on same flow — no forced page break)
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Investor Readiness", "\u25CE", S)

    inv_rows = [
        [Paragraph("<b>Metric</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])],
        [Paragraph("Overall Score", S["Body"]),
         Paragraph(f'<b><font color="#{score_color(overall_score).hexval()[2:]}">{int(overall_score)}/100</font></b>', S["Body"])],
        [Paragraph("Investment Readiness", S["Body"]),
         Paragraph(f'<b><font color="#{score_color(readiness_num * 10).hexval()[2:]}">{readiness_raw}/10</font></b>', S["Body"])],
        [Paragraph("Investment Outlook", S["Body"]), Paragraph(v({"o": outlook}, "o"), S["Body"])],
        [Paragraph("Funding Stage", S["Body"]), Paragraph(v(investor, "funding_stage"), S["Body"])],
        [Paragraph("Recommended Raise", S["Body"]), Paragraph(v({"r": raise_amount}, "r"), S["Body"])],
        [Paragraph("Investment Risk", S["Body"]),
         Paragraph(f'<b><font color="#{risk_color(risk_level).hexval()[2:]}">{str(risk_level).upper()}</font></b>', S["Body"])],
    ]
    inv_t = Table(inv_rows, colWidths=[180, PAGE_W - 2 * MARGIN - 180])
    inv_t.setStyle(two_col_detail_style())
    C.append(inv_t)
    C.append(Spacer(1, 14))

    # Strengths & Weaknesses
    sw_t = Table([[
        list_cell("STRENGTHS",  investor.get("strengths", []),  GREEN,  S),
        list_cell("WEAKNESSES", investor.get("weaknesses", []), ORANGE, S),
    ]], colWidths=[col2, col2])
    sw_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), ORANGE_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(sw_t)
    C.append(Spacer(1, 14))

    # Investment Risks
    C.append(Paragraph("Investment Risks", S["SubHeader"]))
    C += bullet_list(investor.get("risks", []), S["BodySmall"])
    C.append(Spacer(1, 10))

    # AI Recommendations
    C.append(Paragraph("AI Recommendations", S["SubHeader"]))
    recs = investor.get("recommendations", [])
    if recs:
        for i, rec in enumerate(recs, 1):
            C.append(Paragraph(f'<b><font color="#0078D4">{i}.</font></b>  {rec}', S["Body"]))
            C.append(Spacer(1, 3))
    else:
        C.append(Paragraph("No AI recommendations available.", S["BodySmall"]))

    C.append(Spacer(1, 20))

    # ── Final Disclaimer ─────────────────────────────────────────────────────
    disclaimer = Table([[
        Paragraph(
            '<b>Generated by ChiefAI \u2014 AI Startup Intelligence Platform</b>  \u2022  '
            'Powered by Microsoft Azure AI Foundry  \u2022  '
            'Confidential \u2022 For Evaluation Purposes Only',
            ParagraphStyle("Disc", fontName="Helvetica", fontSize=7.5,
                           textColor=GRAY_TEXT, leading=11, alignment=TA_CENTER)),
    ]], colWidths=[PAGE_W - 2 * MARGIN])
    disclaimer.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), GRAY_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BOX",           (0, 0), (-1, -1), 0.4, GRAY_BORDER),
    ]))
    C.append(disclaimer)

    # ── Build ────────────────────────────────────────────────────────────────
    pdf.build(
        C,
        onFirstPage=add_header_footer,
        onLaterPages=add_header_footer,
    )

    return filename
