# from reportlab.platypus import (
#     SimpleDocTemplate,
#     Paragraph,
#     Spacer,
#     Table,
#     TableStyle,
#     PageBreak,
# )

# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet

# from app.database.db import get_connection
# import json


# def add_header_footer(
#     canvas,
#     doc
# ):

#     canvas.saveState()

#     canvas.setFont(
#         "Helvetica",
#         9
#     )

#     canvas.drawString(
#         40,
#         820,
#         "ChiefAI • Microsoft Azure AI Foundry • Confidential"
#     )

#     canvas.drawRightString(
#     560,
#     20,
#     f"ChiefAI | Page {canvas.getPageNumber()}"
#     )

#     canvas.restoreState()

# def export_report_pdf(report_id):

#     conn = get_connection()

#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT * FROM startup_reports WHERE id=?",
#         (report_id,)
#     )

#     report = cursor.fetchone()

#     conn.close()

#     if not report:
#         raise Exception(
#             f"Report {report_id} not found"
#         )

#     data = json.loads(
#         report["report_json"]
#     )

#     market = data.get(
#         "market",
#         {}
#     )

#     business = data.get(
#         "business",
#         {}
#     )

#     investor = data.get(
#         "investor",
#         {}
#     )

#     filename = (
#         f"report_{report_id}.pdf"
#     )

#     pdf = SimpleDocTemplate(
#         filename
#     )

#     styles = getSampleStyleSheet()

#     # ==================================================
#     # MICROSOFT THEME
#     # ==================================================

#     styles["Heading1"].textColor = colors.HexColor("#0078D4")
#     styles["Heading2"].textColor = colors.HexColor("#106EBE")

#     content = []

#     # ==================================================
#     # COVER PAGE
#     # ==================================================

#     score = int(investor.get("readiness_score", 0))

#     overall_score = score * 5 + 50

#     confidence = min(95, 80 + score)

#     if overall_score >= 80:
#         outlook = "Strong Investment Opportunity"

#     elif overall_score >= 60:
#         outlook = "Promising Startup"

#     else:
#         outlook = "Needs Improvement"


#     # --------------------------------------------------
#     # ChiefAI Branding
#     # --------------------------------------------------

#     content.append(
#     Paragraph(
#         "ChiefAI",
#         styles["Title"]
#     )
#     )

#     content.append(
#     Paragraph(
#         "AI Startup Intelligence Report",
#         styles["Heading1"]
#     )
#     )

#     content.append(
#     Paragraph(
#         "Powered by Microsoft Azure AI Foundry",
#         styles["Heading2"]
#     )
#     )

#     content.append(
#     Paragraph(
#         "<font color='#0078D4'><b>12 Specialized AI Agents • Microsoft Azure AI Foundry • Enterprise Startup Intelligence Platform</b></font>",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1, 12)
#     )

#     content.append(
#     Paragraph(
#         "<font color='#0078D4'>__________________________________________________________</font>",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1, 20)
#     )

#     # --------------------------------------------------
#     # Overall Startup Score
#     # --------------------------------------------------

#     content.append(
#     Paragraph(
#         "Overall Startup Score",
#         styles["Heading2"]
#     )
#     )

#     content.append(
#     Paragraph(
#         f"<font size='30'><b>{overall_score}/100</b></font>",
#         styles["Title"]
#     )
#     )

#     content.append(
#     Spacer(1, 10)
#     )

#     content.append(
#     Paragraph(
#         outlook,
#         styles["Heading2"]
#     )
#     )

#     content.append(
#     Spacer(1, 12)
#     )

#     # --------------------------------------------------
#     # AI Summary
#     # --------------------------------------------------

#     content.append(
#     Paragraph(
#         f"<b>AI Confidence Score:</b> {confidence}%",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#         f"<b>AI Agents Executed:</b> {len(data.get('execution_log', []))}",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#         f"<b>Platform:</b> Microsoft Azure AI Foundry Multi-Agent Architecture",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1, 18)
#     )

#     content.append(
#     Paragraph(
#         "<font color='#D0D0D0'>__________________________________________________________</font>",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1, 12)
#     )

#     # --------------------------------------------------
#     # Report Information
#     # --------------------------------------------------

#     content.append(
#     Paragraph(
#         f"<b>Report ID:</b> {report_id}",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#         f"<b>Generated On:</b> {data['metadata']['generated_at']}",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#         f"<b>Platform Version:</b> {data['metadata'].get('version', '2.0')}",
#         styles["BodyText"]
#     )
#     )

#     content.append(
#         Paragraph(
#             "<font color='#106EBE'><b>Generated using Microsoft's Azure AI Foundry, Azure OpenAI, and a ChiefAI Multi-Agent Intelligence Architecture.</b></font>",
#             styles["BodyText"]
#         )
#     )

#     content.append(
#         Spacer(1, 25)
#     )

#     content.append(
#     Spacer(1, 30)
#     )

#     # ==================================================
#     # KPI DASHBOARD
#     # ==================================================

#     kpi_table = Table(
#         [
#             [
#                 f"Overall Score\n\n⭐ {overall_score}/100",

#                 f"Market Size\n\n{market.get('market_size','-')}",

#                 f"Growth Rate\n\n{market.get('growth_rate','-')}"
#             ],

#             [
#                 f"Funding Stage\n\n💰{investor.get('funding_stage','-')}",

#                 f"Raise\n\n{investor.get('recommended_raise','-')}",

#                 f"Risk\n\n⚠ {investor.get('investment_risk','-')}"
#             ]
#         ],
#         colWidths=[170,170,170]
#     )

#     kpi_table.setStyle(
#         TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )
    
#     content.append(kpi_table)
    
#     content.append(
#         Paragraph(
#             "Azure AI Executive Summary",
#             styles["Heading2"]
#         )
#     )

#     verdict_summary = f"""
#         This startup operates in a market of
#         {market.get('market_size','-')}
#         with projected growth of
#         {market.get('growth_rate','-')}.
#     """

#     content.append(
#         Paragraph(
#             verdict_summary,
#             styles["BodyText"]
#         )
#     )

#     content.append(
#         Spacer(1,12)
#     )

#     advantages = business.get("key_advantages", [])

#     for item in advantages:
#         content.append(
#             Paragraph(f"• {item}", styles["BodyText"])
#         )

#     verdict_table = Table(
#     [
#         ["Investment Decision"],
#         [
#             f"""
#     Investment Rating

#     A+

#     {outlook}

#     Recommended Stage

#     {investor.get('funding_stage','-')}

#     Confidence

#     {confidence}%
#     """
#             ]
#         ],
#         colWidths=[500]
#     )

#     verdict_table.setStyle(
#         TableStyle([
#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),
#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),
#             ("GRID",(0,0),(-1,-1),1,colors.black),
#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
#             ("BOTTOMPADDING",(0,1),(-1,-1),15),
#         ])
#     )

#     content.append(verdict_table)
        

#     content.append(
#         Spacer(1,25)
#     )


#     # ==================================================
#     # AI AGENT EXECUTION SUMMARY
#     # ==================================================

#     content.append(
#         Paragraph(
#             "AI Agent Execution Summary",
#             styles["Heading1"]
#         )
#     )

#     execution_data = [
#         ["AI Agent", "Status", "Execution Time"]
#     ]

#     for log in data.get("execution_log", []):

#         execution_data.append([
#             log.get("agent", "-"),
#             "✅ Completed" if log.get("status") == "Completed" else "❌ Failed",
#             f"{log.get('execution_time', '-')} sec"
#         ])

#     execution_table = Table(
#         execution_data,
#         colWidths=[220,120,160]
#     )

#     execution_table.setStyle(
#         TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(execution_table)

#     content.append(
#         Spacer(1,20)
#     )

#     # ==================================================
#     # ANALYSIS METADATA
#     # ==================================================

#     metadata = data.get("metadata", {})

#     content.append(
#         Paragraph(
#             "Analysis Metadata",
#             styles["Heading1"]
#         )
#     )

#     metadata_table = Table(
#     [
#     ["Property","Value"],

#     ["Platform",
#     metadata.get("platform","ChiefAI")],

#     ["Version",
#     metadata.get("version","2.0")],

#     ["Powered By",
#     "Microsoft Azure AI Foundry"],

#     ["AI Agents",
#     str(len(metadata.get("agents_used",[])))],

#     ["Analysis Time",
#     f"{metadata.get('analysis_time','-')} sec"],

#     ["Generated",
#     metadata.get("generated_at","-")]
#     ],
#     colWidths=[180,320]
#     )

#     metadata_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(metadata_table)

#     content.append(
#     Spacer(1,20)
#     )

#     content.append(
#         Paragraph(
#             "AI Confidence Score",
#             styles["Heading1"]
#         )
#     )
#     content.append(
#     Paragraph(
#     f"""
#     <font size="24">
#     <b>{confidence}%</b>
#     </font>
#     <br/>
#     Generated using Microsoft Azure AI Foundry Multi-Agent Intelligence
#     """,
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,20)
#     )



#     # ==================================================
#     # EXECUTIVE SUMMARY
#     # ==================================================

#     content.append(
#         Paragraph(
#         "Executive Summary",
#         styles["Heading1"]
#         )
#     )

#     executive_summary = f"""
#     <b>Business Overview</b><br/><br/>

#     This startup operates in a market worth
#     <b>{market.get('market_size','-')}</b>
#     with an expected annual growth rate of
#     <b>{market.get('growth_rate','-')}</b>.

#     The company targets
#     <b>{business.get('target_customer','-')}</b>
#     through a
#     <b>{business.get('business_model','-')}</b>.

#     Current investor readiness is
#     <b>{score}/10</b>,
#     placing the startup in the
#     <b>{outlook}</b> category.

#     The startup demonstrates strong product-market fit,
#     clear customer value proposition,
#     and scalable business potential.

#     Key focus areas include strengthening
#     competitive differentiation, validating
#     customer acquisition channels, and
#     expanding strategic partnerships.
#     """

#     content.append(
#         Paragraph(
#             executive_summary,
#             styles["BodyText"]
#         )
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # STARTUP SCORECARD
#     # ==================================================

#     content.append(
#     Paragraph(
#         "AI Investment Scorecard",
#         styles["Heading1"]
#         )
#     )

#     market_score = 8 if market else 5

#     business_score = 8 if business else 5

#     competition_score = 7 if market.get("competitors") else 5

#     scalability_score = min(
#         10,
#         score + 1
#     )


#     scorecard = Table(
#         [["Category", "Score"],
#         ["Market Opportunity", f"{market_score}/10"],
#         ["Business Model", f"{business_score}/10"],
#         ["Scalability", f"{scalability_score}/10"],
#         ["Competitive Advantage", f"{competition_score}/10"],
#         ["Investor Readiness", f"{score}/10"],
#         ["Overall Score", f"{overall_score}/100"]],
#         colWidths=[300,200]
#     )

#     scorecard.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(scorecard)

#     content.append(
#     Spacer(1,20)
#     )

#     content.append(PageBreak())

#     # ==================================================
#     # MARKET OPPORTUNITY
#     # ==================================================

#     content.append(
#         Paragraph(
#             "Market Opportunity",
#             styles["Heading1"]
#         )
#     )

#     content.append(
#         Paragraph(
#             "<b>Market Attractiveness Score: 8/10</b>",
#             styles["Heading2"]
#         )
#     )

#     content.append(
#         Spacer(1,10)
#     )

#     market_table = Table(
#         [
#             ["Metric", "Value"],

#             [
#                 "Market Size",
#                 market.get(
#                     "market_size",
#                     "-"
#                 )
#             ],

#             [
#                 "Growth Rate",
#                 market.get(
#                     "growth_rate",
#                     "-"
#                 )
#             ],

#             [
#                 "TAM",
#                 market.get(
#                     "tam",
#                     "-"
#                 )
#             ],

#             [
#                 "SAM",
#                 market.get(
#                     "sam",
#                     "-"
#                 )
#             ],

#             [
#                 "SOM",
#                 market.get(
#                     "som",
#                     "-"
#                 )
#             ]
#         ],
#         colWidths=[180, 320]
#     )

#     market_table.setStyle(
#         TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#         market_table
#     )

#     content.append(
#         Spacer(1,20)
#     )

#     # ==================================================
#     # TAM SAM SOM EXPLANATION
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Market Sizing Analysis",
#     styles["Heading2"]
#     )
#     )

#     content.append(
#     Paragraph(
#     f"<b>TAM:</b> {market.get('tam_explanation','-')}",
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#     f"<b>SAM:</b> {market.get('sam_explanation','-')}",
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Paragraph(
#     f"<b>SOM:</b> {market.get('som_explanation','-')}",
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # COMPETITIVE LANDSCAPE
#     # ==================================================

#     content.append(Paragraph("Competitive Landscape",styles["Heading1"]))

#     competitors = market.get("competitors",[])

#     if competitors:
#         competitor_table = Table([["Competitor"]]+[[c] for c in competitors],colWidths=[500])
#         competitor_table.setStyle(
#             TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#         )
#         content.append(competitor_table)
#         content.append(Spacer(1,20))
#         content.append(Paragraph("<b>Competitive Advantage</b>",styles["Heading2"]))

#     advantages = business.get("key_advantages", [])

#     if advantages:

#         for item in advantages:

#             content.append(
#                 Paragraph(
#                     f"• {item}",
#                     styles["BodyText"]
#                 )
#             )

#     else:

#         content.append(
#             Paragraph(
#                 "No competitive advantages identified.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(
#         Spacer(1,20)
#     )

#     # ==================================================
#     # MARKET TRENDS
#     # ==================================================

#     content.append(
#         Paragraph(
#             "Market Trends",
#             styles["Heading2"]
#         )
#     )

#     trends = market.get("market_trends", [])

#     if trends:
#         for trend in trends:
#             content.append(
#                 Paragraph(
#                     f"• {trend}",
#                     styles["BodyText"]
#                 )
#             )
#     else:
#         content.append(
#             Paragraph(
#                 "No market trends identified.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(Spacer(1,20))

#     # ==================================================
#     # MARKET RISKS
#     # ==================================================

#     content.append(
#     Paragraph(
#             "Market Risks",
#             styles["Heading1"]
#         )
#     )

#     risks = market.get("risks", [])

#     if risks:
#         for risk in risks:
#             content.append(
#                 Paragraph(
#                     f"• {risk}",
#                     styles["BodyText"]
#                 )
#             )
#     else:
#         content.append(
#             Paragraph(
#                 "No significant market risks identified.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(
#         Spacer(1,20)
#     )

#     # ==================================================
#     # Opportunities
#     # ==================================================
#     content.append(
#         Paragraph(
#             "Market Opportunities",
#             styles["Heading2"]
#         )
#     )

#     opportunities = market.get("opportunities", [])

#     if opportunities:
#         for item in opportunities:
#             content.append(
#                 Paragraph(
#                     f"• {item}",
#                     styles["BodyText"]
#                 )
#             )
#     else:
#         content.append(
#             Paragraph(
#                 "No major opportunities identified.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(
#         Spacer(1,20)
#     )

    
    
#     # ==================================================
#     # SWOT ANALYSIS
#     # ==================================================

#     swot = data.get(
#     "swot",
#     {}
#     )

#     content.append(
#     Paragraph(
#     "SWOT Analysis",
#     styles["Heading1"]
#     )
#     )

#     content.append(
#     Paragraph(
#     """
#     SWOT analysis provides a strategic
#     overview of the startup's internal
#     strengths and weaknesses along with
#     external opportunities and threats.
#     """,
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,15)
#     )

#     strengths_text = "\n".join(
#         swot.get("strengths", [])
#     )

#     weaknesses_text = "\n".join(
#         swot.get("weaknesses", [])
#     )

#     opportunities_text = "\n".join(
#         swot.get("opportunities", [])
#     )

#     threats_text = "\n".join(
#         swot.get("threats", [])
#     )

#     swot_table = Table(
#         [
#             ["Strengths","Weaknesses"],
#             [strengths_text, weaknesses_text],
#             ["Opportunities","Threats"],
#             [opportunities_text, threats_text]
#         ],
#         colWidths=[250,250]
#     )

#     swot_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     swot_table
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # SWOT INSIGHT
#     # ==================================================

#     content.append(
#         Paragraph(
#             "Strategic Insight",
#             styles["Heading2"]
#         )
#     )

#     executive_summary += f"""

#     <br/><br/>

#     This report was automatically generated
#     through collaborative reasoning between
#     multiple specialized AI agents running
#     on Microsoft's Azure AI Foundry.
#     """

#     content.append(
#         Paragraph(
#             executive_summary,
#             styles['BodyText']
#         )
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # STARTUP NARRATIVE
#     # ==================================================

#     presentation = data.get(
#     "presentation",
#     {}
#     )

#     content.append(
#     Paragraph(
#     "Startup Narrative",
#     styles["Heading1"]
#     )
#     )

#     narrative_table = Table(
#     [
#     [
#     "Elevator Pitch",
#     presentation.get(
#         "elevator_pitch",
#         "-"
#     )
#     ],

#     [
#     "Problem",
#     presentation.get(
#         "problem",
#         "-"
#     )
#     ],

#     [
#     "Solution",
#     presentation.get(
#         "solution",
#         "-"
#     )
#     ],

#     [
#     "Traction",
#     presentation.get(
#         "traction",
#         "-"
#     )
#     ],

#     [
#     "Funding Ask",
#     presentation.get(
#         "ask",
#         "-"
#     )
#     ]
#     ],
#     colWidths=[140,360]
#     )

#     narrative_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     narrative_table
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # BUSINESS STRATEGY
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Business Strategy",
#     styles["Heading1"]
#     )
#     )

#     strategy_table = Table(
#     [
#     [
#     "Business Model",
#     business.get(
#         "business_model",
#         "-"
#     )
#     ],

#     [
#     "Target Customer",
#     business.get(
#         "target_customer",
#         "-"
#     )
#     ],

#     [
#     "Growth Strategy",
#     business.get(
#         "growth_strategy",
#         "-"
#     )
#     ]
#     ],
#     colWidths=[150,350]
#     )

#     strategy_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     strategy_table
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # REVENUE MODEL
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Revenue Streams",
#     styles["Heading2"]
#     )
#     )

#     streams = business.get("revenue_streams", [])

#     if streams:
#         for stream in streams:
#             content.append(
#                 Paragraph(
#                     f"• {stream}",
#                     styles["BodyText"]
#                 )
#             )
#     else:
#         content.append(
#             Paragraph(
#                 "No revenue streams identified.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(Spacer(1,20))

#     # ==================================================
#     # GO TO MARKET STRATEGY
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Go-To-Market Strategy",
#     styles["Heading1"]
#     )
#     )

#     content.append(
#     Paragraph(
#     business.get(
#     "go_to_market",
#     "-"
#     ),
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,15)
#     )

#     # ==================================================
#     # CUSTOMER SEGMENTS
#     # ==================================================

#     content.append(Paragraph("Customer Segments",styles["Heading2"]))

#     segments = business.get("customer_segments", [])

#     if not segments:
#         segments = ["No customer segments identified"]

#     customer_table = Table(
#         [["Segment"]] +
#         [[segment] for segment in segments],
#         colWidths=[500]
#     )

#     customer_table.setStyle(
#         TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(customer_table)

#     content.append(Spacer(1,20))

#     # ==================================================
#     # ACQUISITION CHANNELS
#     # ==================================================

#     content.append(Paragraph("Acquisition Channels",styles["Heading2"]))

#     channels = business.get("acquisition_channels", [])

#     if not channels:
#         channels = ["No acquisition channels identified"]

#     channel_table = Table(
#         [["Channel"]] +
#         [[channel] for channel in channels],
#         colWidths=[500]
#     )

#     channel_table.setStyle(
#         TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )


#     content.append(channel_table)
#     content.append(Spacer(1,20))

#     # ==================================================
#     # PRICING & PARTNERSHIPS
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Pricing Strategy",
#     styles["Heading2"]
#     )
#     )

#     content.append(
#     Paragraph(
#     business.get(
#     "pricing_strategy",
#     "-"
#     ),
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,10)
#     )

#     content.append(
#     Paragraph(
#     "Partnership Strategy",
#     styles["Heading2"]
#     )
#     )

#     content.append(
#     Paragraph(
#     business.get(
#     "partnership_strategy",
#     "-"
#     ),
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,20)
#     )
#     # ==================================================
#     # INVESTOR READINESS DASHBOARD
#     # ==================================================

#     content.append(PageBreak())

#     content.append(
#         Paragraph(
#             "Investor Readiness",
#             styles["Heading1"]
#         )
#     )

#     readiness_table = Table(
#     [
#     ["Metric", "Value"],

#     [
#     "Readiness Score",
#     f"{investor.get('readiness_score','-')}/10"
#     ],

#     [
#     "Funding Stage",
#     investor.get(
#         "funding_stage",
#         "-"
#     )
#     ],

#     [
#     "Recommended Raise",
#     investor.get(
#         "recommended_raise",
#         "-"
#     )
#     ],

#     [
#     "Investment Risk",
#     investor.get(
#         "investment_risk",
#         "-"
#     )
#     ]
#     ],
#     colWidths=[220,280]
#     )

#     readiness_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(readiness_table)

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # STRENGTHS VS IMPROVEMENTS
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Investment Analysis",
#     styles["Heading1"]
#     )
#     )

#     analysis_table = Table(
#     [
#     [
#     "Strengths",
#     "Areas For Improvement"
#     ],

#     [
#     "\n".join(
#         investor.get(
#             "strengths",
#             []
#         )
#     ),

#     "\n".join(
#         investor.get(
#             "weaknesses",
#             []
#         )
#     )
#     ]
#     ],
#     colWidths=[250,250]
#     )

#     analysis_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     analysis_table
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # AI RECOMMENDATIONS
#     # ==================================================

#     content.append(
#         Paragraph(
#             "AI Strategic Recommendations",
#             styles["Heading1"]
#         )
#     )

#     recommendations = investor.get("recommendations", [])

#     if recommendations:
#         for rec in recommendations:
#             content.append(
#                 Paragraph(
#                     f"• {rec}",
#                     styles["BodyText"]
#                 )
#             )
#     else:
#         content.append(
#             Paragraph(
#                 "No strategic recommendations available.",
#                 styles["BodyText"]
#             )
#         )

#     content.append(Spacer(1,20))

#     # ==================================================
#     # FUNDING RECOMMENDATION
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Funding Recommendation",
#     styles["Heading1"]
#     )
#     )

#     funding_table = Table(
#     [
#     ["Category", "Recommendation"],

#     [
#     "Stage",
#     investor.get(
#         "funding_stage",
#         "-"
#     )
#     ],

#     [
#     "Raise Amount",
#     investor.get(
#         "recommended_raise",
#         "-"
#     )
#     ],

#     [
#     "Risk",
#     investor.get(
#         "investment_risk",
#         "-"
#     )
#     ]
#     ],
#     colWidths=[180,320]
#     )

#     funding_table.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     funding_table
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # USE OF FUNDS
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Suggested Use Of Funds",
#     styles["Heading2"]
#     )
#     )

#     use_of_funds = Table(
#     [
#     ["Area", "Allocation"],

#     ["Product Development", "40%"],

#     ["Marketing & Growth", "25%"],

#     ["Hiring & Talent", "20%"],

#     ["Operations", "15%"]
#     ],
#     colWidths=[250,250]
#     )

#     use_of_funds.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(use_of_funds)

#     content.append(
#     Spacer(1,20)
#     )

#     # ==================================================
#     # RISK ASSESSMENT
#     # ==================================================

#     risk = investor.get(
#     "investment_risk",
#     "Unknown"
#     )

#     if risk.lower() == "low":
#         risk_display = (
#         '<font color="green">'
#         '🟢 LOW RISK'
#         '</font>'
#         )

#     elif risk.lower() in ["medium","moderate"]:
#         risk_display = (
#         '<font color="orange">'
#         '🟡 MODERATE RISK'
#         '</font>'
#         )

#     else:
#         risk_display = (
#         '<font color="red">'
#         '🔴 HIGH RISK'
#         '</font>'
#         )

#     content.append(Paragraph("Risk Assessment",styles["Heading1"]))
#     content.append(Paragraph(risk_display,styles["BodyText"]))
#     content.append(Spacer(1,20))

#     # ==================================================
#     # INVESTMENT VERDICT
#     # ==================================================

#     content.append(
#     Paragraph(
#     "Investment Verdict",
#     styles["Heading1"]
#     )
#     )

#     if overall_score >= 80:
#         verdict = """
#         Strong investment opportunity with
#         scalable growth potential, strong
#         market demand, and attractive
#         investor readiness.
#         """
#     elif overall_score >= 60:
#         verdict = """
#         Promising startup with moderate
#         investment readiness and strong
#         future growth potential.
#         """
#     else:
#         verdict = """
#         Startup demonstrates market
#         potential but requires stronger
#         traction, validation, and customer
#         acquisition evidence before
#         significant investment.
#         """

#     content.append(Paragraph(verdict,styles["BodyText"]))
#     content.append(Spacer(1,20))

#     # ==================================================
#     # 90 DAY ACTION PLAN
#     # ==================================================

#     content.append(
#     Paragraph("90-Day Action Plan",
#     styles["Heading1"]
#     ))

#     action_plan = Table(
#     [[
#     "Days 1-30",
#     "Validate pricing model with customers"],

#     ["Days 31-60",
#     "Secure university and ecosystem partnerships"],

#     ["Days 61-90",
#     "Launch referral growth engine and investor outreach"]],
#     colWidths=[120,380]
#     )

#     action_plan.setStyle(
#     TableStyle([

#             ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),

#             ("TEXTCOLOR",(0,0),(-1,0),colors.white),

#             ("GRID",(0,0),(-1,-1),1,colors.black),

#             ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

#             ("BOTTOMPADDING",(0,0),(-1,0),10),

#             ("TOPPADDING",(0,0),(-1,-1),8),

#             ("ROWBACKGROUNDS",
#             (0,1),
#             (-1,-1),
#             [
#             colors.whitesmoke,
#             colors.HexColor("#F8F8F8")
#             ])
#         ])
#     )

#     content.append(
#     action_plan
#     )

#     content.append(
#     Spacer(1,30)
#     )

#     content.append(
#     PageBreak()
#     )

#     content.append(
#     Paragraph(
#     "ChiefAI Multi-Agent AI Architecture",
#     styles["Heading1"]
#     )
#     )

#     architecture = """
#     This report was generated using Microsoft's
#     Azure AI Foundry multi-agent architecture.

#     Specialized AI agents collaborated to produce
#     this report:

#     • Azure AI Research Agent

#     • Azure AI Market Intelligence Agent

#     • Azure AI Business Strategy Agent

#     • Azure AI SWOT Analysis Agent

#     • Azure AI Funding Strategy Agent

#     • Azure AI Investor Readiness Agent

#     • Azure AI Risk Assessment Agent

#     • Azure AI Executive Summary Agent

#     The final report combines the outputs from all
#     specialized agents into a single investor-ready
#     startup intelligence report.
#     """

#     content.append(
#     Paragraph(
#     architecture,
#     styles["BodyText"]
#     )
#     )

#     content.append(
#     Spacer(1,20)
#     )

#     content.append(
#     Paragraph(
#         "<b>• Microsoft AI Services Utilized</b>",
#         styles["Heading2"]
#     )
# )

#     content.append(
#         Paragraph(
#             """
#             • Microsoft Azure AI Foundry

#             • Azure OpenAI Service

#             • Azure AI Agent Service

#             • Azure AI Search (Extensible)

#             • FastAPI Backend

#             • SQLite Storage

#             • Multi-Agent Orchestration

#             • Investor Intelligence Engine

#             • PDF Report Generation
#             """,
#             styles["BodyText"]
#         )
#     )

#     # ==================================================
#     # FINAL FOOTER
#     # ==================================================

#     content.append(
#         Paragraph(
#             "<font size='9' color='gray'><b>Generated by ChiefAI Multi-Agent Intelligence Platform</b></font>",
#             styles["BodyText"]
#         )
#     )

#     content.append(
#         Paragraph(
#             "<font size='9' color='gray'>Confidential • For Evaluation Purposes Only</font>",
#             styles["BodyText"]
#         )
#     )

#     content.append(
#         Paragraph(
#             "Powered by Microsoft Azure AI Foundry",
#             styles["BodyText"]
#         )
#     )



#     pdf.build(
#         content,
#         onFirstPage=add_header_footer,
#         onLaterPages=add_header_footer
#     )

#     return filename

# Fixed Code

"""
ChiefAI — Microsoft Azure AI Foundry
PDF Export Service  •  Hackathon Edition
"""

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
    KeepTogether,
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas as pdf_canvas

from app.database.db import get_connection
import json
from datetime import datetime

# ── Brand Palette ──────────────────────────────────────────────────────────────

BLUE         = colors.HexColor("#0078D4")   # Microsoft primary blue
BLUE_DARK    = colors.HexColor("#005A9E")   # Darker blue for headers
BLUE_LIGHT   = colors.HexColor("#E5F1FB")   # Very light blue for alt rows
GREEN        = colors.HexColor("#107C10")   # Success / strengths
GREEN_LIGHT  = colors.HexColor("#DFF6DD")
ORANGE       = colors.HexColor("#FF8C00")   # Warning / medium risk
ORANGE_LIGHT = colors.HexColor("#FFF4CE")
RED          = colors.HexColor("#D13438")   # Danger / high risk
RED_LIGHT    = colors.HexColor("#FDE7E9")
PURPLE       = colors.HexColor("#8764B8")   # Accent
TEAL         = colors.HexColor("#00B7C3")   # Accent 2
GRAY_TEXT    = colors.HexColor("#605E5C")   # Body secondary
GRAY_DARK    = colors.HexColor("#323130")   # Body primary
GRAY_BG      = colors.HexColor("#F3F2F1")   # Background
GRAY_BORDER  = colors.HexColor("#E1DFDD")
WHITE        = colors.white

PAGE_W, PAGE_H = A4
MARGIN        = 18 * mm

# ── Style Builder ──────────────────────────────────────────────────────────────

def build_styles():
    styles = getSampleStyleSheet()

    def add(name, **kw):
        styles.add(ParagraphStyle(name=name, **kw))

    # Page-level headings
    add("ChiefTitle",
        fontName="Helvetica-Bold", fontSize=32, textColor=WHITE,
        leading=40, spaceAfter=4, alignment=TA_LEFT)

    add("ChiefSubtitle",
        fontName="Helvetica", fontSize=13, textColor=colors.HexColor("#C7E0F4"),
        leading=18, spaceAfter=2, alignment=TA_LEFT)

    add("SectionHeader",
        fontName="Helvetica-Bold", fontSize=14, textColor=BLUE_DARK,
        leading=18, spaceBefore=14, spaceAfter=6, alignment=TA_LEFT)

    add("SubHeader",
        fontName="Helvetica-Bold", fontSize=11, textColor=GRAY_DARK,
        leading=15, spaceBefore=8, spaceAfter=4, alignment=TA_LEFT)

    add("Body",
        fontName="Helvetica", fontSize=9.5, textColor=GRAY_DARK,
        leading=14, spaceAfter=3, alignment=TA_LEFT)

    add("BodySmall",
        fontName="Helvetica", fontSize=8.5, textColor=GRAY_TEXT,
        leading=12, spaceAfter=2, alignment=TA_LEFT)

    add("BulletItem",
        fontName="Helvetica", fontSize=9.5, textColor=GRAY_DARK,
        leading=14, spaceAfter=2, leftIndent=10, firstLineIndent=-10)

    add("KpiValue",
        fontName="Helvetica-Bold", fontSize=26, textColor=GRAY_DARK,
        leading=30, spaceAfter=2, alignment=TA_CENTER)

    add("KpiLabel",
        fontName="Helvetica-Bold", fontSize=7.5, textColor=GRAY_TEXT,
        leading=10, spaceAfter=0, alignment=TA_CENTER)

    add("BadgeBlue",
        fontName="Helvetica-Bold", fontSize=8, textColor=BLUE,
        leading=11, spaceAfter=0, alignment=TA_CENTER)

    add("ScoreBig",
        fontName="Helvetica-Bold", fontSize=48, textColor=WHITE,
        leading=56, spaceAfter=0, alignment=TA_CENTER)

    add("ScoreLabel",
        fontName="Helvetica-Bold", fontSize=10, textColor=colors.HexColor("#C7E0F4"),
        leading=14, spaceAfter=0, alignment=TA_CENTER)

    add("FooterText",
        fontName="Helvetica", fontSize=7.5, textColor=GRAY_TEXT,
        leading=10, spaceAfter=0, alignment=TA_CENTER)

    add("CoverTag",
        fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
        leading=11, spaceAfter=0, alignment=TA_CENTER)

    return styles


# ── Table Style Factory ────────────────────────────────────────────────────────

def std_table_style(header_bg=BLUE, alt_row=BLUE_LIGHT):
    """Standard polished table style used across all tables."""
    return TableStyle([
        # Header row
        ("BACKGROUND",    (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 9),
        ("TOPPADDING",    (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 9),
        ("ALIGN",         (0, 0), (-1, 0), "LEFT"),
        # Body rows
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("TOPPADDING",    (0, 1), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 7),
        ("ALIGN",         (0, 1), (-1, -1), "LEFT"),
        ("TEXTCOLOR",     (0, 1), (-1, -1), GRAY_DARK),
        # Alternating rows
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, alt_row]),
        # Grid
        ("LINEBELOW",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (-1, -1), 0.4, GRAY_BORDER),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("ROWHEIGHT",     (0, 0), (-1, -1), 6),
    ])


def two_col_detail_style():
    """Left-label, right-value table used for detail sections."""
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


# ── Score / Outlook helpers ────────────────────────────────────────────────────

def score_color(n):
    if n >= 75: return GREEN
    if n >= 50: return ORANGE
    return RED

def score_color_light(n):
    if n >= 75: return GREEN_LIGHT
    if n >= 50: return ORANGE_LIGHT
    return RED_LIGHT

def risk_color(risk: str):
    r = risk.lower()
    if "low" in r:    return GREEN
    if "medium" in r or "moderate" in r: return ORANGE
    return RED

def risk_label(risk: str):
    r = risk.lower()
    if "low" in r:    return "LOW RISK"
    if "medium" in r or "moderate" in r: return "MODERATE RISK"
    return "HIGH RISK"

def outlook_label(score: int) -> str:
    if score >= 80: return "Strong Investment Opportunity"
    if score >= 60: return "Promising Startup"
    return "Needs Improvement"

def fmt_dt(s: str) -> str:
    try:
        return datetime.fromisoformat(s).strftime("%B %d, %Y  %H:%M UTC")
    except Exception:
        return s

def v(d: dict, key: str, default="-") -> str:
    val = d.get(key, default)
    return str(val) if val else default

def bullet_lines(items: list, style, prefix="  \u2022  ") -> list:
    out = []
    for item in items:
        out.append(Paragraph(f"{prefix}{item}", style))
    return out


# ── Drawing Helpers (canvas-level) ────────────────────────────────────────────

def draw_score_ring(c, x, y, r, pct, fg_color, bg_color=None):
    """Draw a circular progress ring using canvas arcs."""
    import math
    bg = bg_color or colors.HexColor("#E1DFDD")
    c.setStrokeColor(bg)
    c.setLineWidth(6)
    c.circle(x, y, r, stroke=1, fill=0)
    if pct > 0:
        c.setStrokeColor(fg_color)
        c.setLineWidth(6)
        start = 90
        end = 90 - (pct / 100) * 360
        # Draw arc using bezier approximation via path
        c.saveState()
        c.setLineCap(1)  # round caps
        from reportlab.graphics.shapes import ArcPath
        # Simple approach: draw a series of short arcs
        steps = max(1, int(abs(pct) * 3.6))
        for i in range(steps):
            a1 = math.radians(start - i * (pct * 3.6 / steps))
            a2 = math.radians(start - (i + 1) * (pct * 3.6 / steps))
            x1 = x + r * math.cos(a1)
            y1 = y + r * math.sin(a1)
            x2 = x + r * math.cos(a2)
            y2 = y + r * math.sin(a2)
            c.line(x1, y1, x2, y2)
        c.restoreState()


def draw_progress_bar(c, x, y, w, h, pct, fill_color, bg_color=None):
    """Draw a horizontal progress bar."""
    bg = bg_color or colors.HexColor("#E1DFDD")
    # Background
    c.setFillColor(bg)
    c.roundRect(x, y, w, h, h/2, stroke=0, fill=1)
    # Fill
    if pct > 0:
        c.setFillColor(fill_color)
        fill_w = max(h, w * min(pct, 100) / 100)
        c.roundRect(x, y, fill_w, h, h/2, stroke=0, fill=1)


# ── Header / Footer ───────────────────────────────────────────────────────────

def add_header_footer(canv, doc):
    canv.saveState()
    w, h = A4

    # Top bar
    canv.setFillColor(BLUE_DARK)
    canv.rect(0, h - 22, w, 22, stroke=0, fill=1)

    canv.setFont("Helvetica-Bold", 8)
    canv.setFillColor(WHITE)
    canv.drawString(MARGIN, h - 15, "ChiefAI  \u2022  Microsoft Azure AI Foundry  \u2022  Confidential")
    canv.drawRightString(w - MARGIN, h - 15, "AI Startup Intelligence Report")

    # Bottom bar
    canv.setFillColor(GRAY_BG)
    canv.rect(0, 0, w, 18, stroke=0, fill=1)
    canv.setFillColor(GRAY_TEXT)
    canv.setFont("Helvetica", 7.5)
    canv.drawString(MARGIN, 6, "Generated by ChiefAI  \u2022  Powered by Microsoft Azure AI Foundry  \u2022  Confidential")
    canv.drawRightString(w - MARGIN, 6, f"Page {canv.getPageNumber()}")

    # Thin accent line under top bar
    canv.setStrokeColor(TEAL)
    canv.setLineWidth(1.5)
    canv.line(0, h - 23, w, h - 23)

    canv.restoreState()


def add_cover_footer(canv, doc):
    """Cover page has no page number — just a bottom accent."""
    canv.saveState()
    w, h = A4
    canv.setFillColor(BLUE_DARK)
    canv.rect(0, 0, w, 14, stroke=0, fill=1)
    canv.setFillColor(WHITE)
    canv.setFont("Helvetica", 7)
    canv.drawCentredString(w / 2, 4,
        "Confidential  \u2022  For Evaluation Purposes Only  \u2022  ChiefAI \u00a9 2025")
    canv.restoreState()


# ── KPI Card helper ───────────────────────────────────────────────────────────

def kpi_card_table(cards: list, styles, col_count=4) -> Table:
    """
    cards = list of (label, value, sub, accent_color)
    Returns a Table of KPI cards arranged in col_count columns.
    """
    s = styles
    rows = []
    for i in range(0, len(cards), col_count):
        chunk = cards[i:i + col_count]
        while len(chunk) < col_count:
            chunk.append(("", "", "", WHITE))

        label_row, value_row, sub_row = [], [], []
        for (label, value, sub, color) in chunk:
            label_row.append(Paragraph(label, s["KpiLabel"]))
            vp = Paragraph(f'<font color="#{color.hexval()[2:]}">{value}</font>', s["KpiValue"]) if value else Paragraph("—", s["KpiValue"])
            value_row.append(vp)
            sub_row.append(Paragraph(sub or "", s["BodySmall"]))

        rows.extend([label_row, value_row, sub_row])

    col_w = (PAGE_W - 2 * MARGIN) / col_count
    t = Table(rows, colWidths=[col_w] * col_count)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), WHITE),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (-2, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        # Top accent bars per column — drawn via LINEABOVE
        *[("LINEABOVE", (j, 0), (j, 0), 4, cards[j][3] if j < len(cards) else BLUE)
          for j in range(min(col_count, len(cards)))],
    ]))
    return t


# ── Reusable Section Title Block ──────────────────────────────────────────────

def section_title(title: str, icon: str, styles) -> list:
    """Returns [HRule, Title paragraph, small spacer]."""
    return [
        HRFlowable(width="100%", thickness=0.5, color=GRAY_BORDER, spaceAfter=6),
        Paragraph(f'<font color="#0078D4">{icon}</font>  {title}', styles["SectionHeader"]),
        Spacer(1, 4),
    ]


def badge_paragraph(text: str, bg: colors.Color, fg: colors.Color, styles) -> Table:
    """A small colored badge as a 1-cell Table."""
    p = Paragraph(f'<b>{text}</b>', ParagraphStyle(
        "BadgeInline", fontName="Helvetica-Bold", fontSize=8,
        textColor=fg, leading=11, alignment=TA_CENTER))
    t = Table([[p]], colWidths=[120])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), bg),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BOX",           (0, 0), (-1, -1), 0.4, fg),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return t


# ── SWOT 2×2 Table ────────────────────────────────────────────────────────────

def build_swot_table(swot: dict, styles) -> Table:
    s_items  = swot.get("strengths", [])
    w_items  = swot.get("weaknesses", [])
    op_items = swot.get("opportunities", [])
    th_items = swot.get("threats", [])

    def cell(title, items, fg, bg):
        lines = [Paragraph(f'<b><font color="#{fg.hexval()[2:]}">{title}</font></b>',
                           styles["SubHeader"])]
        for it in items:
            lines.append(Paragraph(f'  \u2022  {it}', styles["BodySmall"]))
        if not items:
            lines.append(Paragraph("  \u2022  No data available.", styles["BodySmall"]))
        return lines

    col_w = (PAGE_W - 2 * MARGIN) / 2

    t = Table([
        [cell("STRENGTHS", s_items, GREEN, GREEN_LIGHT),
         cell("WEAKNESSES", w_items, RED, RED_LIGHT)],
        [cell("OPPORTUNITIES", op_items, BLUE, BLUE_LIGHT),
         cell("THREATS", th_items, ORANGE, ORANGE_LIGHT)],
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


# ── Score Bar (visual progress) ───────────────────────────────────────────────

def score_bar_table(label: str, pct: float, styles, color=None) -> Table:
    col = color or score_color(pct)
    filled = max(1, int(round((PAGE_W - 2 * MARGIN - 160) * min(pct, 100) / 100)))
    total  = int(PAGE_W - 2 * MARGIN - 160)
    empty  = max(0, total - filled)

    bar_row = Table(
        [[Paragraph("", styles["Body"]), Paragraph("", styles["Body"])]],
        colWidths=[filled, empty] if empty > 0 else [total]
    )
    bar_row.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), col),
        ("BACKGROUND", (1, 0), (1, 0), GRAY_BG),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("BOX",           (0, 0), (-1, -1), 0.3, GRAY_BORDER),
    ]))

    t = Table([[
        Paragraph(label, styles["BodySmall"]),
        bar_row,
        Paragraph(f'<b>{int(pct)}%</b>', ParagraphStyle(
            "PctRight", fontName="Helvetica-Bold", fontSize=8.5,
            textColor=col, leading=11, alignment=TA_RIGHT)),
    ]], colWidths=[130, total, 30])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


# ── Agent Status Table ────────────────────────────────────────────────────────

def build_agent_table(execution_log: list, styles) -> Table:
    if not execution_log:
        return Paragraph("No execution log available.", styles["BodySmall"])

    rows = [[
        Paragraph("<b>AI Agent</b>", styles["Body"]),
        Paragraph("<b>Status</b>", styles["Body"]),
        Paragraph("<b>Time (sec)</b>", styles["Body"]),
    ]]
    for log in execution_log:
        status = log.get("status", "Unknown")
        is_ok  = status.lower() == "completed"
        status_p = Paragraph(
            f'<font color="{"#107C10" if is_ok else "#D13438"}"><b>{"✓ Completed" if is_ok else "✕ Failed"}</b></font>',
            styles["Body"])
        rows.append([
            Paragraph(log.get("agent", "-"), styles["Body"]),
            status_p,
            Paragraph(str(log.get("execution_time", "-")), styles["Body"]),
        ])

    t = Table(rows, colWidths=[280, 120, 100])
    style = std_table_style()
    # Color completed rows light green
    for i, log in enumerate(execution_log, start=1):
        if log.get("status", "").lower() == "completed":
            style.add("BACKGROUND", (0, i), (-1, i), GREEN_LIGHT)
        else:
            style.add("BACKGROUND", (0, i), (-1, i), RED_LIGHT)
    t.setStyle(style)
    return t


# ── Competitor Table ──────────────────────────────────────────────────────────

def build_competitor_table(competitors: list, styles) -> Table:
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
            name     = str(c)
            strength = "-"
        rows.append([
            Paragraph(str(i), styles["Body"]),
            Paragraph(f'<b><font color="#0078D4">{name}</font></b>', styles["Body"]),
            Paragraph(strength, styles["BodySmall"]),
        ])

    t = Table(rows, colWidths=[25, 160, 315])
    t.setStyle(std_table_style())
    return t


# ── Main Export Function ───────────────────────────────────────────────────────

def export_report_pdf(report_id) -> str:
    # ── Fetch data ──────────────────────────────────────────────────────────
    conn   = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM startup_reports WHERE id=?", (report_id,))
    report = cursor.fetchone()
    conn.close()

    if not report:
        raise Exception(f"Report {report_id} not found")

    data     = json.loads(report["report_json"])
    market   = data.get("market",   {})
    business = data.get("business", {})
    investor = data.get("investor", {})
    swot     = data.get("swot",     {})
    overview = data.get("overview", {})
    presentation = data.get("presentation", {})
    metadata = data.get("metadata", {})
    exec_log = data.get("execution_log", [])

    # ── Derived scores ──────────────────────────────────────────────────────
    readiness_raw = investor.get("readiness_score", 0)
    readiness_num = float(str(readiness_raw).replace("%", "") or 0)
    overall_score = int(overview.get("overall_score", min(100, readiness_num * 10)))
    confidence    = float(str(overview.get("ai_confidence", min(95, 80 + readiness_num))).replace("%", "") or 75)
    outlook       = overview.get("investment_outlook", outlook_label(overall_score))
    risk_raw      = investor.get("investment_risk", investor.get("risk_level", "Unknown"))

    completed_agents = sum(1 for l in exec_log if l.get("status", "").lower() == "completed")

    # ── Styles ──────────────────────────────────────────────────────────────
    S = build_styles()

    # ── Document setup ──────────────────────────────────────────────────────
    filename = f"chiefai_report_{report_id}.pdf"
    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=30 * mm, bottomMargin=20 * mm,
        title=f"ChiefAI Startup Report #{report_id}",
        author="ChiefAI — Microsoft Azure AI Foundry",
        subject="AI Startup Intelligence Report",
    )

    C = []  # content list

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 1 — COVER
    # ══════════════════════════════════════════════════════════════════════════

    # Full-bleed cover header block (simulated with a wide table)
    cover_bg = Table(
        [[
            Paragraph("ChiefAI", S["ChiefTitle"]),
        ]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    cover_bg.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLUE_DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 20),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 16),
    ]))
    C.append(cover_bg)

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

    # Teal accent strip
    accent_strip = Table(
        [[Paragraph(
            "  12 Specialized AI Agents  \u2022  Microsoft Azure AI Foundry  \u2022  Enterprise Startup Intelligence",
            S["CoverTag"])]],
        colWidths=[PAGE_W - 2 * MARGIN],
    )
    accent_strip.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), TEAL),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    C.append(accent_strip)
    C.append(Spacer(1, 18))

    # ── Cover Score Panel ────────────────────────────────────────────────────
    sc = score_color(overall_score)
    score_cell = [
        Paragraph(f'<font color="#FFFFFF"><b>{overall_score}</b></font>', ParagraphStyle(
            "CoverScore", fontName="Helvetica-Bold", fontSize=52, textColor=WHITE,
            leading=58, alignment=TA_CENTER)),
        Paragraph('<font color="#C7E0F4">/ 100  Overall Score</font>', ParagraphStyle(
            "CoverScoreSub", fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#C7E0F4"),
            leading=14, alignment=TA_CENTER)),
        Spacer(1, 6),
        Paragraph(f'<font color="#FFFFFF"><b>{outlook}</b></font>', ParagraphStyle(
            "CoverOutlook", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE,
            leading=16, alignment=TA_CENTER)),
    ]
    info_cell = [
        Paragraph(f'<b>Report ID:</b>  #{report_id}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Generated:</b>  {fmt_dt(metadata.get("generated_at", "-"))}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Platform Version:</b>  {metadata.get("version", "2.0")}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>AI Agents Executed:</b>  {completed_agents} / {max(len(exec_log), 12)}', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>Analysis Time:</b>  {metadata.get("analysis_time", "-")} sec', S["Body"]),
        Spacer(1, 4),
        Paragraph(f'<b>AI Confidence:</b>  {confidence:.0f}%', S["Body"]),
        Spacer(1, 12),
        Paragraph(
            '<font color="#005A9E"><b>Powered by Microsoft Azure AI Foundry</b><br/>'
            'Azure OpenAI  \u2022  Azure AI Agent Service  \u2022  Multi-Agent Orchestration</font>',
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

    # ── Cover KPI Strip ──────────────────────────────────────────────────────
    kpi_data = [
        [
            Paragraph("<b>Market Size</b>",     S["KpiLabel"]),
            Paragraph("<b>Growth Rate</b>",      S["KpiLabel"]),
            Paragraph("<b>Funding Stage</b>",    S["KpiLabel"]),
            Paragraph("<b>Recommended Raise</b>", S["KpiLabel"]),
        ],
        [
            Paragraph(v(market,   "market_size"),        S["KpiValue"]),
            Paragraph(v(market,   "growth_rate"),        S["KpiValue"]),
            Paragraph(v(investor, "funding_stage"),      S["KpiValue"]),
            Paragraph(v(investor, "recommended_raise",
                        investor.get("raise_amount", "-")), S["KpiValue"]),
        ],
        [
            Paragraph("Total Addressable Market",  S["BodySmall"]),
            Paragraph("CAGR",                      S["BodySmall"]),
            Paragraph("AI Recommended Stage",      S["BodySmall"]),
            Paragraph("Target Capital",            S["BodySmall"]),
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

    # ── Investment Decision Banner ───────────────────────────────────────────
    invest_color = score_color(overall_score)
    decision_text = (
        "STRONG INVEST" if overall_score >= 80
        else "CONSIDER INVEST" if overall_score >= 60
        else "NEEDS IMPROVEMENT"
    )
    risk_c = risk_color(risk_raw) if risk_raw != "Unknown" else GRAY_TEXT

    decision_table = Table(
        [[
            Paragraph(f'<font color="#FFFFFF"><b>AI INVESTMENT DECISION:  {decision_text}</b></font>',
                      ParagraphStyle("Decision", fontName="Helvetica-Bold", fontSize=11,
                                     textColor=WHITE, leading=15, alignment=TA_CENTER)),
            Paragraph(f'<font color="#FFFFFF">Risk:  <b>{risk_raw.upper()}</b></font>',
                      ParagraphStyle("RiskTag", fontName="Helvetica-Bold", fontSize=9,
                                     textColor=WHITE, leading=13, alignment=TA_CENTER)),
        ]],
        colWidths=[(PAGE_W - 2 * MARGIN) * 0.72, (PAGE_W - 2 * MARGIN) * 0.28],
    )
    decision_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), invest_color),
        ("BACKGROUND",    (1, 0), (1, 0), risk_c),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("BOX",           (0, 0), (-1, -1), 0, WHITE),
    ]))
    C.append(decision_table)

    C.append(Spacer(1, 20))

    # ── Confidence / Readiness bars ──────────────────────────────────────────
    C.append(Paragraph("AI Analysis Confidence", S["SubHeader"]))
    C.append(Spacer(1, 4))
    C.append(score_bar_table("AI Confidence Score",      confidence,    S, BLUE))
    C.append(Spacer(1, 3))
    C.append(score_bar_table("Investment Readiness",     readiness_num * 10 if readiness_num <= 10 else readiness_num, S, GREEN))
    C.append(Spacer(1, 3))
    C.append(score_bar_table("Overall Startup Score",    overall_score, S, sc))

    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 2 — AI AGENT EXECUTION + EXECUTIVE SUMMARY
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("AI Agent Execution Summary", "\u26A1", S)
    C.append(Paragraph(
        f'<b>{completed_agents}</b> of <b>{max(len(exec_log), 12)}</b> specialized AI agents '
        f'completed analysis on Microsoft Azure AI Foundry.', S["Body"]))
    C.append(Spacer(1, 8))
    C.append(build_agent_table(exec_log, S))
    C.append(Spacer(1, 16))

    # ── AI Confidence Metadata ───────────────────────────────────────────────
    meta_rows = [
        ["Platform",       metadata.get("platform",        "ChiefAI")],
        ["Version",        metadata.get("version",         "2.0")],
        ["Powered By",     "Microsoft Azure AI Foundry"],
        ["AI Agents",      str(len(metadata.get("agents_used", exec_log or [])))],
        ["Analysis Time",  f'{metadata.get("analysis_time", "-")} sec'],
        ["Generated",      fmt_dt(metadata.get("generated_at", "-"))],
        ["AI Confidence",  f"{confidence:.0f}%"],
    ]
    meta_t = Table(
        [[Paragraph("<b>Property</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])]]
        + [[Paragraph(r[0], S["Body"]), Paragraph(r[1], S["Body"])] for r in meta_rows],
        colWidths=[160, PAGE_W - 2 * MARGIN - 160],
    )
    meta_t.setStyle(two_col_detail_style())
    C.append(meta_t)
    C.append(Spacer(1, 18))

    # ── Executive Summary ────────────────────────────────────────────────────
    C += section_title("Executive Summary", "\u2139", S)

    exec_summary = overview.get("executive_summary") or (
        f'This startup operates in a market of <b>{v(market, "market_size")}</b> '
        f'with projected CAGR of <b>{v(market, "growth_rate")}</b>. '
        f'The company targets <b>{v(business, "target_customer")}</b> '
        f'via a <b>{v(business, "business_model")}</b>. '
        f'Current investor readiness score: <b>{readiness_raw}</b>, '
        f'placing the startup in the <b>{outlook}</b> category.'
    )
    C.append(Paragraph(exec_summary, S["Body"]))
    C.append(Spacer(1, 10))

    # Startup narrative quick summary
    if presentation:
        narr_rows = [
            [Paragraph("<b>Field</b>",  S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
            [Paragraph("Elevator Pitch", S["Body"]), Paragraph(v(presentation, "elevator_pitch"), S["Body"])],
            [Paragraph("Problem",        S["Body"]), Paragraph(v(presentation, "problem"),        S["Body"])],
            [Paragraph("Solution",       S["Body"]), Paragraph(v(presentation, "solution"),       S["Body"])],
            [Paragraph("Traction",       S["Body"]), Paragraph(v(presentation, "traction"),       S["Body"])],
            [Paragraph("Funding Ask",    S["Body"]), Paragraph(v(presentation, "ask"),            S["Body"])],
        ]
        narr_t = Table(narr_rows, colWidths=[110, PAGE_W - 2 * MARGIN - 110])
        narr_t.setStyle(two_col_detail_style())
        C.append(narr_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 3 — AI INVESTMENT SCORECARD + MARKET OPPORTUNITY
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("AI Investment Scorecard", "\u2605", S)

    market_sc = min(10, 5 + (1 if market else 0) + (1 if market.get("tam") else 0) +
                    (1 if market.get("growth_rate") else 0) + (1 if market.get("competitors") else 0))
    biz_sc    = min(10, 5 + (1 if business.get("business_model") else 0) +
                    (1 if business.get("revenue_streams") else 0) + (1 if business.get("go_to_market") else 0))
    comp_sc   = min(10, 5 + len(market.get("competitors", [])))
    scale_sc  = min(10, max(5, int(readiness_num) + 1))

    scorecard_rows = [
        [Paragraph("<b>Category</b>", S["Body"]),
         Paragraph("<b>Score</b>",    S["Body"]),
         Paragraph("<b>Visual</b>",   S["Body"])],
    ]
    for (cat, sc_val, max_v) in [
        ("Market Opportunity",    market_sc,  10),
        ("Business Model",        biz_sc,     10),
        ("Scalability",           scale_sc,   10),
        ("Competitive Advantage", comp_sc,    10),
        ("Investor Readiness",    int(readiness_num), 10),
        ("Overall Score",         overall_score, 100),
    ]:
        pct  = (sc_val / max_v) * 100
        col  = score_color(pct)
        bar  = score_bar_table("", pct, S, col)
        scorecard_rows.append([
            Paragraph(cat, S["Body"]),
            Paragraph(f'<b><font color="#{col.hexval()[2:]}">{sc_val}/{max_v}</font></b>', S["Body"]),
            bar,
        ])

    sc_t = Table(scorecard_rows, colWidths=[170, 70, PAGE_W - 2 * MARGIN - 240])
    sc_t.setStyle(std_table_style())
    C.append(sc_t)
    C.append(Spacer(1, 16))

    # ── Market Opportunity ───────────────────────────────────────────────────
    C += section_title("Market Opportunity", "\u2316", S)

    mkt_rows = [
        [Paragraph("<b>Metric</b>", S["Body"]), Paragraph("<b>Value</b>", S["Body"])],
        [Paragraph("Market Size",  S["Body"]), Paragraph(v(market, "market_size"),  S["Body"])],
        [Paragraph("Growth Rate",  S["Body"]), Paragraph(v(market, "growth_rate"),  S["Body"])],
        [Paragraph("TAM",          S["Body"]), Paragraph(v(market, "tam"),          S["Body"])],
        [Paragraph("SAM",          S["Body"]), Paragraph(v(market, "sam"),          S["Body"])],
        [Paragraph("SOM",          S["Body"]), Paragraph(v(market, "som"),          S["Body"])],
    ]
    mkt_t = Table(mkt_rows, colWidths=[160, PAGE_W - 2 * MARGIN - 160])
    mkt_t.setStyle(std_table_style())
    C.append(mkt_t)
    C.append(Spacer(1, 10))

    # TAM/SAM/SOM explanations
    for (label, key) in [("TAM", "tam_explanation"), ("SAM", "sam_explanation"), ("SOM", "som_explanation")]:
        txt = market.get(key)
        if txt:
            C.append(Paragraph(f'<b><font color="#0078D4">{label}:</font></b>  {txt}', S["Body"]))
    C.append(Spacer(1, 10))

    # Market trends / opportunities / risks side-by-side
    def list_cell(title, items, fg):
        lines = [Paragraph(f'<b><font color="#{fg.hexval()[2:]}">{title}</font></b>', S["SubHeader"])]
        for it in (items or ["None identified."]):
            lines.append(Paragraph(f'  \u2022  {it}', S["BodySmall"]))
        return lines

    col3 = (PAGE_W - 2 * MARGIN) / 3
    trends_t = Table([[
        list_cell("MARKET TRENDS",   market.get("market_trends",  []), BLUE),
        list_cell("OPPORTUNITIES",   market.get("opportunities",   []), GREEN),
        list_cell("RISKS",           market.get("risks",           []), RED),
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
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 4 — COMPETITIVE LANDSCAPE + SWOT
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Competitive Landscape", "\u26A0", S)
    C.append(build_competitor_table(market.get("competitors", []), S))
    C.append(Spacer(1, 10))

    # Key advantages
    adv = business.get("key_advantages", [])
    if adv:
        C.append(Paragraph("<b>Competitive Advantages</b>", S["SubHeader"]))
        C += bullet_lines(adv, S["BulletItem"])
    C.append(Spacer(1, 16))

    # ── SWOT ──────────────────────────────────────────────────────────────────
    C += section_title("SWOT Analysis", "\u25A6", S)
    C.append(Paragraph(
        "Strategic overview of internal strengths and weaknesses alongside external opportunities and threats.",
        S["Body"]))
    C.append(Spacer(1, 8))
    C.append(build_swot_table(swot or {
        "strengths":     business.get("strengths", []),
        "weaknesses":    business.get("weaknesses", []),
        "opportunities": business.get("opportunities", []),
        "threats":       business.get("threats", []),
    }, S))
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 5 — BUSINESS STRATEGY
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Business Strategy", "\u2630", S)

    biz_rows = [
        [Paragraph("<b>Field</b>", S["Body"]), Paragraph("<b>Detail</b>", S["Body"])],
        [Paragraph("Business Model",     S["Body"]), Paragraph(v(business, "business_model"),      S["Body"])],
        [Paragraph("Target Customer",    S["Body"]), Paragraph(v(business, "target_customer"),     S["Body"])],
        [Paragraph("Value Proposition",  S["Body"]), Paragraph(v(business, "value_proposition"),  S["Body"])],
        [Paragraph("USP",                S["Body"]), Paragraph(v(business, "usp"),                S["Body"])],
        [Paragraph("Growth Strategy",    S["Body"]), Paragraph(v(business, "growth_strategy"),    S["Body"])],
        [Paragraph("Pricing Strategy",   S["Body"]), Paragraph(v(business, "pricing_strategy"),   S["Body"])],
        [Paragraph("Partnership Strategy", S["Body"]), Paragraph(v(business, "partnership_strategy"), S["Body"])],
    ]
    biz_t = Table(biz_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
    biz_t.setStyle(two_col_detail_style())
    C.append(biz_t)
    C.append(Spacer(1, 14))

    # Revenue Streams
    C.append(Paragraph("Revenue Streams", S["SubHeader"]))
    streams = business.get("revenue_streams", [])
    C += bullet_lines(streams, S["BulletItem"]) if streams else [Paragraph("No revenue streams identified.", S["BodySmall"])]
    C.append(Spacer(1, 10))

    # Go-To-Market
    C += section_title("Go-To-Market Strategy", "\u27A4", S)
    C.append(Paragraph(v(business, "go_to_market"), S["Body"]))
    C.append(Spacer(1, 8))

    col2 = (PAGE_W - 2 * MARGIN) / 2

    def list_col(title, items, fg):
        lines = [Paragraph(f'<b><font color="#{fg.hexval()[2:]}">{title}</font></b>', S["SubHeader"])]
        for it in (items or ["None identified."]):
            lines.append(Paragraph(f'  \u2022  {it}', S["BodySmall"]))
        return lines

    gtm_t = Table([[
        list_col("Customer Segments",    business.get("customer_segments", []),    BLUE),
        list_col("Acquisition Channels", business.get("customer_acquisition_channels",
                                          business.get("acquisition_channels", [])), GREEN),
    ]], colWidths=[col2, col2])
    gtm_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), BLUE_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), GREEN_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(gtm_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 6 — INVESTOR READINESS DASHBOARD
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("Investor Readiness Dashboard", "\u25CE", S)

    inv_rows = [
        [Paragraph("<b>Metric</b>",         S["Body"]), Paragraph("<b>Value</b>",  S["Body"])],
        [Paragraph("Readiness Score",        S["Body"]), Paragraph(f'<b><font color="#{score_color(readiness_num * 10 if readiness_num <= 10 else readiness_num).hexval()[2:]}">{readiness_raw}</font></b>', S["Body"])],
        [Paragraph("Overall Score",          S["Body"]), Paragraph(f'<b>{overall_score}/100</b>', S["Body"])],
        [Paragraph("Funding Stage",          S["Body"]), Paragraph(v(investor, "funding_stage"),       S["Body"])],
        [Paragraph("Recommended Raise",      S["Body"]), Paragraph(v(investor, "recommended_raise",
                                                                       investor.get("raise_amount", "-")), S["Body"])],
        [Paragraph("Runway Estimate",        S["Body"]), Paragraph(v(investor, "runway_estimate"),     S["Body"])],
        [Paragraph("Capital Requirement",    S["Body"]), Paragraph(v(investor, "capital_requirement"), S["Body"])],
        [Paragraph("Valuation Estimate",     S["Body"]), Paragraph(v(investor, "valuation_estimate"),  S["Body"])],
        [Paragraph("Investment Outlook",     S["Body"]), Paragraph(v(investor, "investment_outlook",
                                                                       outlook), S["Body"])],
        [Paragraph("Investment Risk",        S["Body"]),
         Paragraph(f'<b><font color="#{risk_color(risk_raw).hexval()[2:]}">{risk_label(risk_raw)}</font></b>',
                   S["Body"])],
    ]
    inv_t = Table(inv_rows, colWidths=[180, PAGE_W - 2 * MARGIN - 180])
    inv_t.setStyle(two_col_detail_style())
    C.append(inv_t)
    C.append(Spacer(1, 14))

    # Readiness bars
    C.append(Paragraph("Readiness Indicators", S["SubHeader"]))
    C.append(Spacer(1, 6))
    for (lbl, val_key, mult) in [
        ("Investment Readiness",    "readiness_score", 10 if readiness_num <= 10 else 1),
        ("Fundraising Readiness",   "fundraising_readiness", 1),
        ("Pitch Readiness",         "pitch_readiness",       1),
        ("Business Readiness",      "business_readiness",    1),
        ("Market Readiness",        "market_readiness",      1),
        ("Technology Readiness",    "technology_readiness",  1),
    ]:
        raw = investor.get(val_key)
        if raw is not None:
            pct = float(str(raw).replace("%", "") or 0) * mult
            C.append(score_bar_table(lbl, pct, S, score_color(pct)))
            C.append(Spacer(1, 3))

    C.append(Spacer(1, 14))

    # Strengths vs Improvement split
    inv_str  = investor.get("strengths",    [])
    inv_weak = investor.get("weaknesses",   investor.get("areas_for_improvement", []))
    analysis_t = Table([[
        list_col("INVESTMENT STRENGTHS",      inv_str,  GREEN),
        list_col("AREAS FOR IMPROVEMENT",     inv_weak, ORANGE),
    ]], colWidths=[col2, col2])
    analysis_t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), GREEN_LIGHT),
        ("BACKGROUND",    (1, 0), (1, 0), ORANGE_LIGHT),
        ("BOX",           (0, 0), (-1, -1), 0.6, GRAY_BORDER),
        ("LINEAFTER",     (0, 0), (0, -1), 0.4, GRAY_BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    C.append(analysis_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 7 — AI STRATEGIC RECOMMENDATIONS + RISK ASSESSMENT
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("AI Strategic Recommendations", "\u2726", S)

    recs = investor.get("recommendations", overview.get("recommendations", []))
    if recs:
        for i, rec in enumerate(recs, 1):
            C.append(Paragraph(f'<b><font color="#0078D4">{i}.</font></b>  {rec}', S["Body"]))
            C.append(Spacer(1, 3))
    else:
        C.append(Paragraph("No strategic recommendations available.", S["BodySmall"]))
    C.append(Spacer(1, 14))

    # Risk Assessment
    C += section_title("Risk Assessment", "\u26A0", S)

    all_risks = []
    for key in ["risks", "business_risks", "operational_risks", "market_risks",
                "financial_risks", "technology_risks"]:
        all_risks += investor.get(key, [])
    if not all_risks:
        all_risks = market.get("risks", [])

    if all_risks:
        risk_rows = [[
            Paragraph("<b>#</b>", S["Body"]),
            Paragraph("<b>Risk</b>", S["Body"]),
        ]]
        for i, r in enumerate(all_risks, 1):
            risk_rows.append([
                Paragraph(str(i), S["Body"]),
                Paragraph(r, S["Body"]),
            ])
        risk_t = Table(risk_rows, colWidths=[25, PAGE_W - 2 * MARGIN - 25])
        risk_t.setStyle(std_table_style(header_bg=RED, alt_row=RED_LIGHT))
        C.append(risk_t)
    else:
        C.append(Paragraph("No significant risks identified.", S["BodySmall"]))
    C.append(Spacer(1, 16))

    # ── 90-Day Action Plan ───────────────────────────────────────────────────
    C += section_title("90-Day Action Plan", "\u25B6", S)

    milestones = investor.get("next_milestones",
                  overview.get("next_milestones", []))
    if milestones and len(milestones) >= 3:
        plan_rows = [
            [Paragraph("<b>Phase</b>", S["Body"]), Paragraph("<b>Action</b>", S["Body"])],
            [Paragraph("Days 1\u201330",  S["Body"]), Paragraph(milestones[0], S["Body"])],
            [Paragraph("Days 31\u201360", S["Body"]), Paragraph(milestones[1], S["Body"])],
            [Paragraph("Days 61\u201390", S["Body"]), Paragraph(milestones[2], S["Body"])],
        ]
    else:
        plan_rows = [
            [Paragraph("<b>Phase</b>", S["Body"]), Paragraph("<b>Action</b>", S["Body"])],
            [Paragraph("Days 1\u201330",  S["Body"]), Paragraph("Validate pricing model with early customers", S["Body"])],
            [Paragraph("Days 31\u201360", S["Body"]), Paragraph("Secure strategic partnerships and distribution channels", S["Body"])],
            [Paragraph("Days 61\u201390", S["Body"]), Paragraph("Launch growth engine and begin investor outreach", S["Body"])],
        ]
    plan_t = Table(plan_rows, colWidths=[110, PAGE_W - 2 * MARGIN - 110])
    plan_t.setStyle(std_table_style(header_bg=PURPLE, alt_row=colors.HexColor("#F4F0FA")))
    C.append(plan_t)
    C.append(Spacer(1, 16))

    # ── Funding Recommendation ───────────────────────────────────────────────
    C += section_title("Funding Recommendation", "\u25CB", S)

    fund_rows = [
        [Paragraph("<b>Category</b>", S["Body"]), Paragraph("<b>Recommendation</b>", S["Body"])],
        [Paragraph("Stage",           S["Body"]), Paragraph(v(investor, "funding_stage"),        S["Body"])],
        [Paragraph("Raise Amount",    S["Body"]), Paragraph(v(investor, "recommended_raise",
                                                              investor.get("raise_amount", "-")), S["Body"])],
        [Paragraph("Capital Use",     S["Body"]), Paragraph(v(investor, "capital_requirement"),  S["Body"])],
        [Paragraph("Risk Level",      S["Body"]), Paragraph(risk_label(risk_raw),                S["Body"])],
        [Paragraph("Investment Verdict", S["Body"]),
         Paragraph(
             'Strong investment opportunity with scalable growth potential.' if overall_score >= 80
             else 'Promising startup with moderate readiness and strong growth potential.' if overall_score >= 60
             else 'Requires stronger traction, validation, and customer acquisition evidence.',
             S["Body"])],
    ]
    fund_t = Table(fund_rows, colWidths=[150, PAGE_W - 2 * MARGIN - 150])
    fund_t.setStyle(two_col_detail_style())
    C.append(fund_t)
    C.append(Spacer(1, 10))

    # Use of funds
    C.append(Paragraph("Suggested Use of Funds", S["SubHeader"]))
    uof_items = investor.get("use_of_funds", [
        "Product Development — 40%",
        "Marketing & Growth — 25%",
        "Hiring & Talent — 20%",
        "Operations — 15%",
    ])
    uof_rows = [[Paragraph("<b>Area</b>", S["Body"]), Paragraph("<b>Allocation</b>", S["Body"])]]
    for item in uof_items:
        if isinstance(item, dict):
            uof_rows.append([Paragraph(item.get("area", "-"), S["Body"]),
                             Paragraph(item.get("allocation", "-"), S["Body"])])
        elif "\u2014" in item or "-" in item:
            parts = item.replace("\u2014", "-").split("-", 1)
            uof_rows.append([Paragraph(parts[0].strip(), S["Body"]),
                             Paragraph(parts[1].strip() if len(parts) > 1 else "-", S["Body"])])
        else:
            uof_rows.append([Paragraph(item, S["Body"]), Paragraph("-", S["Body"])])

    uof_t = Table(uof_rows, colWidths=[260, 240])
    uof_t.setStyle(std_table_style(header_bg=GREEN, alt_row=GREEN_LIGHT))
    C.append(uof_t)
    C.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 8 — MICROSOFT AZURE AI ARCHITECTURE
    # ══════════════════════════════════════════════════════════════════════════

    C += section_title("ChiefAI Multi-Agent Architecture", "\u2699", S)

    arch_text = (
        "This report was generated using Microsoft\u2019s Azure AI Foundry multi-agent "
        "architecture. Specialized AI agents collaborated through an orchestrated reasoning "
        "pipeline to produce this comprehensive startup intelligence report.\n\n"
        "Each agent contributes domain-specific expertise \u2014 from market research and "
        "competitor analysis to investor readiness and risk assessment \u2014 ensuring "
        "every dimension of the startup is evaluated with precision."
    )
    C.append(Paragraph(arch_text, S["Body"]))
    C.append(Spacer(1, 12))

    agents_list = [
        ("Azure AI Research Agent",          "Web research, data gathering, market intelligence"),
        ("Azure AI Market Intelligence Agent","TAM/SAM/SOM analysis, competitor mapping"),
        ("Azure AI Business Strategy Agent", "Business model, GTM strategy, revenue streams"),
        ("Azure AI SWOT Analysis Agent",     "Strengths, weaknesses, opportunities, threats"),
        ("Azure AI Funding Strategy Agent",  "Funding stage, raise amount, use of funds"),
        ("Azure AI Investor Readiness Agent","Readiness scoring, investor pitch preparation"),
        ("Azure AI Risk Assessment Agent",   "Business, market, technology risk evaluation"),
        ("Azure AI Executive Summary Agent", "Synthesis, narrative generation, recommendations"),
    ]
    agent_rows = [
        [Paragraph("<b>Agent</b>", S["Body"]),
         Paragraph("<b>Responsibility</b>", S["Body"]),
         Paragraph("<b>Status</b>", S["Body"])],
    ]
    for (name, role) in agents_list:
        # Match against exec_log if available
        matched = next((l for l in exec_log if name.lower() in l.get("agent", "").lower()), None)
        status_str = matched.get("status", "Completed") if matched else "Completed"
        is_ok = status_str.lower() == "completed"
        agent_rows.append([
            Paragraph(f'<b>{name}</b>', S["Body"]),
            Paragraph(role, S["BodySmall"]),
            Paragraph(
                f'<font color="{"#107C10" if is_ok else "#D13438"}"><b>{"✓ " + status_str}</b></font>',
                S["Body"]),
        ])
    agents_t = Table(agent_rows, colWidths=[180, 230, 90])
    agents_t.setStyle(std_table_style())
    C.append(agents_t)
    C.append(Spacer(1, 16))

    # Microsoft Services
    C.append(Paragraph("Microsoft AI Services Utilized", S["SubHeader"]))
    services = [
        ("Microsoft Azure AI Foundry",   "Primary multi-agent orchestration platform"),
        ("Azure OpenAI Service",          "GPT-4o powered language model inference"),
        ("Azure AI Agent Service",        "Agent lifecycle and tool management"),
        ("Azure AI Search",               "Extensible knowledge retrieval (RAG)"),
        ("FastAPI Backend",               "REST API layer for agent communication"),
        ("Multi-Agent Orchestration",     "Parallel agent execution and result synthesis"),
        ("Investor Intelligence Engine",  "Custom scoring and readiness evaluation"),
        ("PDF Report Generation",         "This export — ReportLab + ChiefAI formatting"),
    ]
    svc_rows = [
        [Paragraph("<b>Service</b>", S["Body"]), Paragraph("<b>Role</b>", S["Body"])],
    ] + [
        [Paragraph(svc[0], S["Body"]), Paragraph(svc[1], S["BodySmall"])]
        for svc in services
    ]
    svc_t = Table(svc_rows, colWidths=[200, PAGE_W - 2 * MARGIN - 200])
    svc_t.setStyle(std_table_style(header_bg=BLUE_DARK, alt_row=BLUE_LIGHT))
    C.append(svc_t)
    C.append(Spacer(1, 20))

    # ── Final Disclaimer ─────────────────────────────────────────────────────
    disclaimer = Table([[
        Paragraph(
            '<b>Generated by ChiefAI Multi-Agent Intelligence Platform</b>  \u2022  '
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
