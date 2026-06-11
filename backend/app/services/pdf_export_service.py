from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from app.database.db import get_connection
import json


from reportlab.platypus import (
    Table,
    TableStyle
)

from reportlab.lib import colors

def add_header_footer(
    canvas,
    doc
):

    canvas.saveState()

    canvas.setFont(
        "Helvetica",
        9
    )

    canvas.drawString(
        40,
        820,
        "ChiefAI Startup Intelligence Platform"
    )

    canvas.drawString(
        500,
        20,
        f"Page {canvas.getPageNumber()}"
    )

    canvas.restoreState()

def export_report_pdf(report_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM startup_reports WHERE id=?",
        (report_id,)
    )

    report = cursor.fetchone()

    conn.close()

    if not report:
        raise Exception(
            f"Report {report_id} not found"
        )

    data = json.loads(
        report["report_json"]
    )

    print("\n===== REPORT JSON =====")
    print(json.dumps(data, indent=2))
    print("=======================\n")

    market = data.get(
        "market",
        {}
    )

    business = data.get(
        "business",
        {}
    )

    investor = data.get(
        "investor",
        {}
    )

    filename = (
        f"report_{report_id}.pdf"
    )

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    # ==================================================
    # MICROSOFT THEME
    # ==================================================

    styles["Heading1"].textColor = colors.HexColor("#0078D4")
    styles["Heading2"].textColor = colors.HexColor("#106EBE")

    content = []

    # ==================================================
    # COVER PAGE
    # ==================================================

    score = int(investor.get("readiness_score",0))

    overall_score = score * 5 + 50

    if overall_score >= 80:
        outlook = "Strong Investment Opportunity"

    elif overall_score >= 60:
        outlook = "Promising Startup"

    else:
        outlook = "Needs Improvement"

    content.append(Paragraph("ChiefAI",styles["Title"]))

    content.append(Paragraph("Startup Intelligence Report",styles["Heading1"]))

    content.append(Paragraph(f"Report #{report_id}",styles["Heading2"]))

    content.append(Spacer(1, 30))

    # ==================================================
    # KPI DASHBOARD
    # ==================================================

    kpi_table = Table(
        [
            [
                f"Startup Score\n\n{overall_score}/100",

                f"Market Size\n\n{market.get('market_size','-')}",

                f"Growth Rate\n\n{market.get('growth_rate','-')}"
            ],

            [
                f"Funding Stage\n\n{investor.get('funding_stage','-')}",

                f"Raise\n\n{investor.get('recommended_raise','-')}",

                f"Risk\n\n{investor.get('investment_risk','-')}"
            ]
        ],
        colWidths=[170,170,170]
    )

    kpi_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0,0),
                (-1,-1),
                colors.HexColor("#0078D4")
            ),

            (
                "TEXTCOLOR",
                (0,0),
                (-1,-1),
                colors.white
            ),

            (
                "ALIGN",
                (0,0),
                (-1,-1),
                "CENTER"
            ),

            (
                "FONTNAME",
                (0,0),
                (-1,-1),
                "Helvetica-Bold"
            ),

            (
                "FONTSIZE",
                (0,0),
                (-1,-1),
                13
            ),

            (
                "TOPPADDING",
                (0,0),
                (-1,-1),
                15
            ),

            (
                "BOTTOMPADDING",
                (0,0),
                (-1,-1),
                15
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.white
            )
        ])
        )
    
    content.append(
        Paragraph(
            "AI Verdict",
            styles["Heading2"]
        )
    )

    verdict_summary = f"""
    This startup operates in a market of
    {market.get('market_size','-')}
    with projected growth of
    {market.get('growth_rate','-')}.

    Key Strengths:
    • AI-powered differentiation
    • Subscription revenue model
    • Large addressable market

    Primary Risks:
    • Competitive pressure
    • User acquisition challenges
    • Product differentiation
    """

    content.append(
        Paragraph(
            verdict_summary,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    content.append(
    Paragraph(
    "Executive Summary",
    styles["Heading1"]
    )
    )

    executive_summary = f"""
    <b>Business Overview</b><br/><br/>

    This startup operates in a market worth
    <b>{market.get('market_size','-')}</b>
    with an expected annual growth rate of
    <b>{market.get('growth_rate','-')}</b>.

    The company targets
    <b>{business.get('target_customer','-')}</b>
    through a
    <b>{business.get('business_model','-')}</b>.

    Current investor readiness is
    <b>{score}/10</b>,
    placing the startup in the
    <b>{outlook}</b> category.

    The opportunity is attractive due to
    strong demand for AI-powered career
    guidance and growing adoption of
    personalized learning solutions.

    Key focus areas include strengthening
    competitive differentiation, validating
    customer acquisition channels, and
    expanding strategic partnerships.
    """

    content.append(
    Paragraph(
    executive_summary,
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # STARTUP SCORECARD
    # ==================================================

    content.append(
    Paragraph(
    "Startup Scorecard",
    styles["Heading1"]
    )
    )

    scorecard = Table(
    [
    ["Category", "Score"],

    ["Market Opportunity", "8/10"],

    ["Business Model", "7/10"],

    ["Scalability", "8/10"],

    ["Competitive Advantage", "6/10"],

    ["Investor Readiness", f"{score}/10"],

    ["Overall Score", f"{overall_score}/100"]
    ],
    colWidths=[300,200]
    )

    scorecard.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "FONTNAME",
    (0,0),
    (-1,0),
    "Helvetica-Bold"
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    )
    ])
    )

    content.append(scorecard)

    content.append(
    Spacer(1,20)
    )

    content.append(PageBreak())

    # ==================================================
    # MARKET OPPORTUNITY
    # ==================================================

    content.append(
        Paragraph(
            "Market Opportunity",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "<b>Market Attractiveness Score: 8/10</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1,10)
    )

    market_table = Table(
        [
            ["Metric", "Value"],

            [
                "Market Size",
                market.get(
                    "market_size",
                    "-"
                )
            ],

            [
                "Growth Rate",
                market.get(
                    "growth_rate",
                    "-"
                )
            ],

            [
                "TAM",
                market.get(
                    "tam",
                    "-"
                )
            ],

            [
                "SAM",
                market.get(
                    "sam",
                    "-"
                )
            ],

            [
                "SOM",
                market.get(
                    "som",
                    "-"
                )
            ]
        ],
        colWidths=[180, 320]
    )

    market_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0,0),
                (-1,0),
                colors.HexColor("#0078D4")
            ),

            (
                "TEXTCOLOR",
                (0,0),
                (-1,0),
                colors.white
            ),

            (
                "FONTNAME",
                (0,0),
                (-1,0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0,0),
                (-1,-1),
                1,
                colors.black
            ),

            (
                "ROWBACKGROUNDS",
                (0,1),
                (-1,-1),
                [
                    colors.whitesmoke,
                    colors.lightgrey
                ]
            )
        ])
    )

    content.append(
        market_table
    )

    content.append(
        Spacer(1,20)
    )

    # ==================================================
    # TAM SAM SOM EXPLANATION
    # ==================================================

    content.append(
    Paragraph(
    "Market Sizing Analysis",
    styles["Heading2"]
    )
    )

    content.append(
    Paragraph(
    f"<b>TAM:</b> {market.get('tam_explanation','-')}",
    styles["BodyText"]
    )
    )

    content.append(
    Paragraph(
    f"<b>SAM:</b> {market.get('sam_explanation','-')}",
    styles["BodyText"]
    )
    )

    content.append(
    Paragraph(
    f"<b>SOM:</b> {market.get('som_explanation','-')}",
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # COMPETITIVE LANDSCAPE
    # ==================================================

    content.append(Paragraph("Competitive Landscape",styles["Heading1"]))

    competitors = market.get("competitors",[])

    benchmark_table = Table(
        [
            [
                "Feature",
                "Startup",
                "LinkedIn",
                "Coursera",
                "Udemy"
            ],

            [
                "AI Personalization",
                "9",
                "6",
                "5",
                "4"
            ],

            [
                "Career Guidance",
                "9",
                "7",
                "6",
                "4"
            ],

            [
                "Skill Assessment",
                "8",
                "5",
                "4",
                "3"
            ]
        ]
    )

    if competitors:
        competitor_table = Table([["Competitor"]]+[[c] for c in competitors],colWidths=[500])
        competitor_table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),1,colors.black),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")]))
        content.append(competitor_table)
        content.append(Spacer(1,20))
        content.append(Paragraph("<b>Competitive Advantage</b>",styles["Heading2"]))

    for item in business.get("key_advantages",[]):
        content.append(Paragraph(f"• {item}",styles["BodyText"]))
        content.append(Spacer(1,20))

    # ==================================================
    # MARKET TRENDS
    # ==================================================

    content.append(Paragraph("Market Trends",styles["Heading1"]))

    for trend in market.get("market_trends",[]):
        content.append(Paragraph(f"• {trend}",styles["BodyText"]))

    content.append(Spacer(1,20))

    # ==================================================
    # MARKET RISKS
    # ==================================================

    content.append(
    Paragraph(
    "Market Risks",
    styles["Heading1"]
    )
    )

    for risk in market.get("risks",[]):
        content.append(Paragraph(f"• {risk}",styles["BodyText"]))

    content.append(Spacer(1,20))

    # ==================================================
    # Opportunities
    # ==================================================
    content.append(
    Paragraph(
    "Market Opportunities",
    styles["Heading2"]
    )
    )

    for item in market.get("opportunities",[]):
        content.append(Paragraph(f"• {item}",styles["BodyText"]))
    
    # ==================================================
    # SWOT ANALYSIS
    # ==================================================

    swot = data.get(
    "swot",
    {}
    )

    content.append(
    Paragraph(
    "SWOT Analysis",
    styles["Heading1"]
    )
    )

    content.append(
    Paragraph(
    """
    SWOT analysis provides a strategic
    overview of the startup's internal
    strengths and weaknesses along with
    external opportunities and threats.
    """,
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,15)
    )

    swot_table = Table(
    [
    "Strengths",
    "Weaknesses"
    ],

    [
        "\n".join(
            [
                f"• {item}"
                for item in swot.get(
                    "strengths",
                    []
                )
            ]
        ),
    ],
    [
        "\n".join(
            [
                f"• {item}"
                for item in swot.get(
                    "Weaknesses",
                    []
                )
            ]
        )
    ],

    [
    "Opportunities",
    "Threats"
    ],

    [
        "\n".join(
            [
                f"• {item}"
                for item in swot.get(
                    "Opportunities",
                    []
                )
            ]
        ),
    ],
    [
        "\n".join(
            [
                f"• {item}"
                for item in swot.get(
                    "threats",
                    []
                )
            ]
        ),
    ],
    colWidths=[250,250]
    )

    swot_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "BACKGROUND",
    (0,2),
    (-1,2),
    colors.HexColor("#106EBE")
    ),

    (
    "TEXTCOLOR",
    (0,2),
    (-1,2),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    ),

    (
    "FONTNAME",
    (0,0),
    (-1,0),
    "Helvetica-Bold"
    ),

    (
    "FONTNAME",
    (0,2),
    (-1,2),
    "Helvetica-Bold"
    ),

    (
    "VALIGN",
    (0,0),
    (-1,-1),
    "TOP"
    )
    ])
    )

    content.append(
    swot_table
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # SWOT INSIGHT
    # ==================================================

    content.append(
    Paragraph(
    "Strategic Insight",
    styles["Heading2"]
    )
    )

    content.append(
    Paragraph(
    """
    The startup demonstrates strong
    potential due to its AI-driven
    differentiation and focus on a
    growing market segment.

    Continued emphasis on strategic
    partnerships, customer acquisition,
    and product innovation will be
    essential to maintain competitive
    advantage and improve investment
    readiness.
    """,
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # STARTUP NARRATIVE
    # ==================================================

    presentation = data.get(
    "presentation",
    {}
    )

    content.append(
    Paragraph(
    "Startup Narrative",
    styles["Heading1"]
    )
    )

    narrative_table = Table(
    [
    [
    "Elevator Pitch",
    presentation.get(
        "elevator_pitch",
        "-"
    )
    ],

    [
    "Problem",
    presentation.get(
        "problem",
        "-"
    )
    ],

    [
    "Solution",
    presentation.get(
        "solution",
        "-"
    )
    ],

    [
    "Traction",
    presentation.get(
        "traction",
        "-"
    )
    ],

    [
    "Funding Ask",
    presentation.get(
        "ask",
        "-"
    )
    ]
    ],
    colWidths=[140,360]
    )

    narrative_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (0,-1),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (0,-1),
    colors.white
    ),

    (
    "FONTNAME",
    (0,0),
    (0,-1),
    "Helvetica-Bold"
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    ),

    (
    "VALIGN",
    (0,0),
    (-1,-1),
    "TOP"
    )
    ])
    )

    content.append(
    narrative_table
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # BUSINESS STRATEGY
    # ==================================================

    content.append(
    Paragraph(
    "Business Strategy",
    styles["Heading1"]
    )
    )

    strategy_table = Table(
    [
    [
    "Business Model",
    business.get(
        "business_model",
        "-"
    )
    ],

    [
    "Target Customer",
    business.get(
        "target_customer",
        "-"
    )
    ],

    [
    "Growth Strategy",
    business.get(
        "growth_strategy",
        "-"
    )
    ]
    ],
    colWidths=[150,350]
    )

    strategy_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (0,-1),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (0,-1),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    ),

    (
    "FONTNAME",
    (0,0),
    (0,-1),
    "Helvetica-Bold"
    )
    ])
    )

    content.append(
    strategy_table
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # REVENUE MODEL
    # ==================================================

    content.append(
    Paragraph(
    "Revenue Streams",
    styles["Heading2"]
    )
    )

    for stream in business.get("revenue_streams",[]):
        content.append(Paragraph(f"• {stream}",styles["BodyText"]))

    content.append(Spacer(1,20))

    # ==================================================
    # GO TO MARKET STRATEGY
    # ==================================================

    content.append(
    Paragraph(
    "Go-To-Market Strategy",
    styles["Heading1"]
    )
    )

    content.append(
    Paragraph(
    business.get(
    "go_to_market",
    "-"
    ),
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,15)
    )

    # ==================================================
    # CUSTOMER SEGMENTS
    # ==================================================

    content.append(Paragraph("Customer Segments",styles["Heading2"]))

    customer_table = Table([["Segment"]]+[[segment] for segment in business.get("customer_segments",[])],colWidths=[500])

    customer_table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#0078D4")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),1,colors.black)]))

    content.append(customer_table)

    content.append(Spacer(1,20))

    # ==================================================
    # ACQUISITION CHANNELS
    # ==================================================

    content.append(Paragraph("Acquisition Channels",styles["Heading2"]))

    channel_table = Table([["Channel"]]+[[channel] for channel in business.get("acquisition_channels",[])],colWidths=[500])

    channel_table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#106EBE")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),1,colors.black)]))

    content.append(channel_table)
    content.append(Spacer(1,20))

    # ==================================================
    # PRICING & PARTNERSHIPS
    # ==================================================

    content.append(
    Paragraph(
    "Pricing Strategy",
    styles["Heading2"]
    )
    )

    content.append(
    Paragraph(
    business.get(
    "pricing_strategy",
    "-"
    ),
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,10)
    )

    content.append(
    Paragraph(
    "Partnership Strategy",
    styles["Heading2"]
    )
    )

    content.append(
    Paragraph(
    business.get(
    "partnership_strategy",
    "-"
    ),
    styles["BodyText"]
    )
    )

    content.append(
    Spacer(1,20)
    )
    # ==================================================
    # INVESTOR READINESS DASHBOARD
    # ==================================================

    content.append(
    Paragraph(
    "Investor Readiness",
    styles["Heading1"]
    )
    )

    readiness_table = Table(
    [
    ["Metric", "Value"],

    [
    "Readiness Score",
    f"{investor.get('readiness_score','-')}/10"
    ],

    [
    "Funding Stage",
    investor.get(
        "funding_stage",
        "-"
    )
    ],

    [
    "Recommended Raise",
    investor.get(
        "recommended_raise",
        "-"
    )
    ],

    [
    "Investment Risk",
    investor.get(
        "investment_risk",
        "-"
    )
    ]
    ],
    colWidths=[220,280]
    )

    readiness_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "FONTNAME",
    (0,0),
    (-1,0),
    "Helvetica-Bold"
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    )
    ])
    )

    content.append(readiness_table)

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # STRENGTHS VS IMPROVEMENTS
    # ==================================================

    content.append(
    Paragraph(
    "Investment Analysis",
    styles["Heading1"]
    )
    )

    analysis_table = Table(
    [
    [
    "Strengths",
    "Areas For Improvement"
    ],

    [
    "\n".join(
        investor.get(
            "strengths",
            []
        )
    ),

    "\n".join(
        investor.get(
            "weaknesses",
            []
        )
    )
    ]
    ],
    colWidths=[250,250]
    )

    analysis_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#106EBE")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    ),

    (
    "FONTNAME",
    (0,0),
    (-1,0),
    "Helvetica-Bold"
    ),

    (
    "VALIGN",
    (0,0),
    (-1,-1),
    "TOP"
    )
    ])
    )

    content.append(
    analysis_table
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # AI RECOMMENDATIONS
    # ==================================================

    content.append(
    Paragraph(
    "AI Strategic Recommendations",
    styles["Heading1"]
    )
    )

    for rec in investor.get("recommendations",[]):
        content.append(Paragraph(f"• {rec}",styles["BodyText"]))

    content.append(Spacer(1,20))

    # ==================================================
    # FUNDING RECOMMENDATION
    # ==================================================

    content.append(
    Paragraph(
    "Funding Recommendation",
    styles["Heading1"]
    )
    )

    funding_table = Table(
    [
    ["Category", "Recommendation"],

    [
    "Stage",
    investor.get(
        "funding_stage",
        "-"
    )
    ],

    [
    "Raise Amount",
    investor.get(
        "recommended_raise",
        "-"
    )
    ],

    [
    "Risk",
    investor.get(
        "investment_risk",
        "-"
    )
    ]
    ],
    colWidths=[180,320]
    )

    funding_table.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    )
    ])
    )

    content.append(
    funding_table
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # USE OF FUNDS
    # ==================================================

    content.append(
    Paragraph(
    "Suggested Use Of Funds",
    styles["Heading2"]
    )
    )

    use_of_funds = Table(
    [
    ["Area", "Allocation"],

    ["Product Development", "40%"],

    ["Marketing & Growth", "25%"],

    ["Hiring & Talent", "20%"],

    ["Operations", "15%"]
    ],
    colWidths=[250,250]
    )

    use_of_funds.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (-1,0),
    colors.HexColor("#106EBE")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (-1,0),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    )
    ])
    )

    content.append(
    use_of_funds
    )

    content.append(
    Spacer(1,20)
    )

    # ==================================================
    # RISK ASSESSMENT
    # ==================================================

    risk = investor.get(
    "investment_risk",
    "Unknown"
    )

    if risk.lower() == "low":
        risk_display = (
        '<font color="green">'
        'LOW RISK'
        '</font>'
        )

    elif risk.lower() in ["medium","moderate"]:
        risk_display = (
        '<font color="orange">'
        'MODERATE RISK'
        '</font>'
        )

    else:
        risk_display = (
        '<font color="red">'
        'HIGH RISK'
        '</font>'
        )

    content.append(Paragraph("Risk Assessment",styles["Heading1"]))
    content.append(Paragraph(risk_display,styles["BodyText"]))
    content.append(Spacer(1,20))

    # ==================================================
    # INVESTMENT VERDICT
    # ==================================================

    content.append(
    Paragraph(
    "Investment Verdict",
    styles["Heading1"]
    )
    )

    if overall_score >= 80:
        verdict = """
        Strong investment opportunity with
        scalable growth potential, strong
        market demand, and attractive
        investor readiness.
        """
    elif overall_score >= 60:
        verdict = """
        Promising startup with moderate
        investment readiness and strong
        future growth potential.
        """
    else:
        verdict = """
        Startup demonstrates market
        potential but requires stronger
        traction, validation, and customer
        acquisition evidence before
        significant investment.
        """

    content.append(Paragraph(verdict,styles["BodyText"]))
    content.append(Spacer(1,20))

    # ==================================================
    # 90 DAY ACTION PLAN
    # ==================================================

    content.append(
    Paragraph(
    "90-Day Action Plan",
    styles["Heading1"]
    )
    )

    action_plan = Table(
    [
    [
    "Days 1-30",
    "Validate pricing model with customers"
    ],

    [
    "Days 31-60",
    "Secure university and ecosystem partnerships"
    ],

    [
    "Days 61-90",
    "Launch referral growth engine and investor outreach"
    ]
    ],
    colWidths=[120,380]
    )

    action_plan.setStyle(
    TableStyle([
    (
    "BACKGROUND",
    (0,0),
    (0,-1),
    colors.HexColor("#0078D4")
    ),

    (
    "TEXTCOLOR",
    (0,0),
    (0,-1),
    colors.white
    ),

    (
    "GRID",
    (0,0),
    (-1,-1),
    1,
    colors.black
    ),

    (
    "FONTNAME",
    (0,0),
    (0,-1),
    "Helvetica-Bold"
    )
    ])
    )

    content.append(
    action_plan
    )

    content.append(
    Spacer(1,30)
    )

    # ==================================================
    # FINAL FOOTER
    # ==================================================

    content.append(
    Paragraph(
    "Generated by ChiefAI Startup Intelligence Platform | Powered by Azure AI Foundry",
    styles["Italic"]
    )
    )

    pdf.build(
        content,
        onFirstPage=add_header_footer,
        onLaterPages=add_header_footer
    )

    return filename