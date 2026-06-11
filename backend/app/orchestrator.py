import time
from concurrent.futures import ThreadPoolExecutor
from app.services.history_service import HistoryService

from app.agents.market_agent import MarketAgent
from app.agents.business_agent import BusinessAgent
from app.agents.presentation_agent import PresentationAgent
from app.agents.investor_agent import InvestorAgent
from app.agents.swot_agent import SWOTAgent


class StartupOrchestrator:

    def run(self, startup_text):

        start = time.time()

        with ThreadPoolExecutor(max_workers=5) as executor:

            market_future = executor.submit(
                MarketAgent().run,
                startup_text
            )

            business_future = executor.submit(
                BusinessAgent().run,
                startup_text
            )

            investor_future = executor.submit(
                InvestorAgent().run,
                startup_text
            )

            presentation_future = executor.submit(
                PresentationAgent().run,
                startup_text
            )

            swot_future = executor.submit(
                SWOTAgent().run,
                startup_text
            )

        market = market_future.result()
        business = business_future.result()
        presentation = presentation_future.result()
        investor = investor_future.result()
        swot = swot_future.result()

        print(
            "Total Analysis Time:",
            round(time.time() - start, 2),
            "seconds"
        )
            
        report = {
            "market": market,
            "business": business,
            "presentation": presentation,
            "swot": swot,
            "investor": investor
        }

        HistoryService.save_report(report)

        return report