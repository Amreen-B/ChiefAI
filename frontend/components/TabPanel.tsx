import Dashboard from "./Dashboard";
import MarketAnalysis from "./MarketAnalysis";
import BusinessStrategy from "./BusinessStrategy";
import InvestorReadiness from "./InvestorReadiness";
import CompareStartups from "./CompareStartups";

type Props = {
  selected: string;
  report: any;
  history: any[];
};

export default function TabPanel({
  selected,
  report,
  history,
}: Props) {

  switch (selected) {

    case "Market Analysis":
      return (
        <MarketAnalysis
          report={report}
        />
      );

    case "Business Strategy":
      return (
        <BusinessStrategy
          report={report}
        />
      );

    case "Investor Readiness":
      return (
        <InvestorReadiness
          report={report}
        />
      );

    case "Compare Startups":
      return (
        <CompareStartups 
        history={history} 
        />
      );

    default:
      return (
        <Dashboard
          report={report}
        />
      );

  }

}