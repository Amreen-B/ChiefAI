import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from app.services.history_service import HistoryService

from app.agents.market_agent import MarketAgent
from app.agents.business_agent import BusinessAgent
from app.agents.presentation_agent import PresentationAgent
from app.agents.investor_agent import InvestorAgent
from app.agents.swot_agent import SWOTAgent

from app.agents.research_agent import ResearchAgent
from app.agents.competitor_agent import CompetitorAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.risk_agent import RiskAgent
from app.agents.funding_agent import FundingAgent
from app.agents.execution_agent import ExecutionAgent
from app.agents.executive_summary_agent import ExecutiveSummaryAgent


class StartupOrchestrator:

    def run(self, startup_text):

        start = time.time()

        execution_log = []
        def execute_agent(name, agent):

            agent_start = time.time()

            try:

                result = agent.run(startup_text)

                execution_log.append({
                    "agent": name,
                    "status": "Completed",
                    "execution_time": round(time.time() - agent_start, 2)
                })

                print(f"✓ {name} completed")

                return result

            except Exception as e:

                execution_log.append({
                    "agent": name,
                    "status": "Failed",
                    "execution_time": round(time.time() - agent_start, 2),
                    "error": str(e)
                })

                print(f"✗ {name} failed")

                return {}

        with ThreadPoolExecutor(max_workers=8) as executor:


            research_future = executor.submit(
                lambda: execute_agent(
                    "Research Agent",
                    ResearchAgent()
                )
            )

            market_future = executor.submit(
                lambda: execute_agent(
                    "Market Agent",
                    MarketAgent()
                )
            )

            business_future = executor.submit(
                lambda: execute_agent(
                    "Business Agent",
                    BusinessAgent()
                )
            )

            presentation_future = executor.submit(
                lambda: execute_agent(
                    "Presentation Agent",
                    PresentationAgent()
                )
            )

            investor_future = executor.submit(
                lambda: execute_agent(
                    "Investor Agent",
                    InvestorAgent()
                )
            )

            swot_future = executor.submit(
                lambda: execute_agent(
                    "SWOT Agent",
                    SWOTAgent()
                )
            )

            competitor_future = executor.submit(
                lambda: execute_agent(
                    "Competitor Agent",
                    CompetitorAgent()
                )
            )

            strategy_future = executor.submit(
                lambda: execute_agent(
                    "Strategy Agent",
                    StrategyAgent()
                )
            )

            risk_future = executor.submit(
                lambda: execute_agent(
                    "Risk Agent",
                    RiskAgent()
                )
            )

            funding_future = executor.submit(
                lambda: execute_agent(
                    "Funding Agent",
                    FundingAgent()
                )
            )

            execution_future = executor.submit(
                lambda: execute_agent(
                    "Execution Agent",
                    ExecutionAgent()
                )
            )

            executive_summary_future = executor.submit(
                lambda: execute_agent(
                    "Executive Summary Agent",
                    ExecutiveSummaryAgent()
                )
            )
        
        research = research_future.result()
        market = market_future.result()
        business = business_future.result()
        presentation = presentation_future.result()
        investor = investor_future.result()
        swot = swot_future.result()
        competitor = competitor_future.result()
        strategy = strategy_future.result()
        risk = risk_future.result()
        funding = funding_future.result()
        execution = execution_future.result()
        executive_summary = executive_summary_future.result()

        print("\nEXECUTIVE SUMMARY REPORT")
        print(executive_summary)


        report = {

            "metadata":{

                "platform": "ChiefAI",
                "version": "2.0",
                "generated_at":datetime.now().isoformat(),
                "analysis_time":round(
                    time.time()-start,
                    2
                ),

                "agents_used":[
                    "Research",
                    "Market",
                    "Business",
                    "Presentation",
                    "Investor",
                    "SWOT",
                    "Competitor",
                    "Strategy",
                    "Risk",
                    "Funding",
                    "Execution",
                    "Executive Summary"
                ]
            },

            "execution_log":execution_log,

            "research":research,

            "market":market,

            "business":business,

            "presentation":presentation,

            "investor":investor,

            "swot":swot,

            "competitor":competitor,

            "strategy":strategy,

            "risk":risk,

            "funding":funding,

            "execution":execution,

            "executive_summary":executive_summary
        }

        report["execution_log"] = sorted(
            execution_log,
            key=lambda x: x["agent"]
        )

        score = investor.get(
            "readiness_score",
            0
        )

        report["analysis_summary"] = {

            "overall_score":score*10,

            "investment_outlook":
                "Strong Opportunity"
                if score>=8
                else "Promising Startup"
                if score>=6
                else "Needs Improvement",

            "risk_level":
                investor.get(
                    "investment_risk",
                    "Unknown"
                ),

            "recommended_stage":
                investor.get(
                    "funding_stage",
                    "-"
                )
        }

        report["analysis_summary"]["agents_completed"] = len(
            [
                log
                for log in execution_log
                if log["status"] == "Completed"
            ]
        )

        report["analysis_summary"]["total_agents"] = len(execution_log)

        print("\n" + "=" * 55)
        print("        ChiefAI Multi-Agent Analysis Engine")
        print("=" * 55)
        print(
            "Total Analysis Time:",
            round(time.time()-start,2),
            "seconds"
        )
        for log in execution_log:
            print(
                f"{log['agent']} - {log['status']} ({log['execution_time']}s)"
            )


        print(f"Overall Startup Score: {report['analysis_summary']['overall_score']}/100")
        print(f"Investment Outlook: {report['analysis_summary']['investment_outlook']}")


        print("=" * 55 + "\n")

        HistoryService.save_report(report)

        return report