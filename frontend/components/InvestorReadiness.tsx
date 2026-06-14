// type Props = {
//   report: any;
// };

// export default function InvestorReadiness({
//   report,
// }: Props) {

//   const investor = report?.investor || {};

//   return (

//     <div className="space-y-6">

//       <h1 className="text-3xl font-semibold text-black">
//         Investor Readiness
//       </h1>

//       <div className="grid grid-cols-3 gap-4">

//         <div className="bg-white p-5 rounded-xl shadow">
//           <p className="text-black">
//             Readiness Score
//           </p>

//           <h2 className="text-4xl font-bold text-green-600">
//             {investor.readiness_score || 0}
//           </h2>
//         </div>

//         <div className="bg-white p-5 rounded-xl shadow">
//           <p className="text-black">
//             Funding Stage
//           </p>

//           <h2 className="text-xl font-bold text-black">
//             {investor.funding_stage || "N/A"}
//           </h2>
//         </div>

//         <div className="bg-white p-5 rounded-xl shadow">
//           <p className="text-black">
//             Recommended Raise
//           </p>

//           <h2 className="text-xl font-bold text-black">
//             {investor.recommended_raise || "N/A"}
//           </h2>
//         </div>

//       </div>

//       <div className="bg-white p-6 rounded-xl shadow">

//         <h2 className="font-semibold text-lg mb-4 text-black">
//           Strengths
//         </h2>

//         <ul className="list-disc ml-6 text-black">
//           {(investor.strengths || []).map(
//             (item: string, index: number) => (
//               <li key={index}>{item}</li>
//             )
//           )}
//         </ul>

//       </div>

//       <div className="bg-white p-6 rounded-xl shadow">

//         <h2 className="font-semibold text-lg mb-4 text-black">
//           Risks
//         </h2>

//         <ul className="list-disc ml-6 text-black">
//           {(investor.risks || []).map(
//             (item: string, index: number) => (
//               <li key={index}>{item}</li>
//             )
//           )}
//         </ul>

//       </div>

//     </div>

//   );

// }

// Fixed Code

// ── TypeScript Interfaces ──────────────────────────────────────────────────────

interface ReadinessItem {
  label: string;
  status: "pass" | "fail" | "partial" | string;
  note?: string;
}

interface InvestorData {
  // Overview
  readiness_score?: string | number;
  overall_score?: string | number;
  investment_outlook?: string;
  funding_stage?: string;
  recommended_raise?: string;
  raise_amount?: string;
  ai_confidence?: string | number;
  risk_level?: string;

  // Funding Analysis
  capital_requirement?: string;
  use_of_funds?: string[];
  runway_estimate?: string;
  valuation_estimate?: string;

  // Investment Metrics
  market_potential?: string;
  revenue_potential?: string;
  scalability?: string;
  traction?: string;
  business_maturity?: string;

  // Strengths
  strengths?: string[];
  competitive_advantages?: string[];
  strongest_points?: string[];

  // Risks
  risks?: string[];
  operational_risks?: string[];
  market_risks?: string[];
  financial_risks?: string[];
  technology_risks?: string[];

  // AI Recommendation
  should_invest?: string | boolean;
  recommendation?: string;
  investment_thesis?: string;
  investment_concerns?: string[];
  suggested_improvements?: string[];

  // Due Diligence
  due_diligence?: {
    product_validation?: string;
    market_validation?: string;
    revenue_validation?: string;
    team_validation?: string;
    financial_validation?: string;
  };
  due_diligence_checklist?: ReadinessItem[];

  // Readiness
  fundraising_readiness?: string | number;
  pitch_readiness?: string | number;
  business_readiness?: string | number;
  market_readiness?: string | number;
  technology_readiness?: string | number;

  // Recommendations
  top_recommendations?: string[];
  improvements_before_fundraising?: string[];
  next_milestones?: string[];
  growth_priorities?: string[];
}

interface Props {
  report: {
    investor?: InvestorData;
    metadata?: {
      generated_at?: string;
      analysis_time?: string | number;
    };
  } | null;
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function val(v: string | number | undefined, fallback = "N/A"): string {
  return v !== undefined && v !== null && String(v).trim() !== ""
    ? String(v)
    : fallback;
}

function arr(v: string[] | undefined): string[] {
  return Array.isArray(v) ? v : [];
}

function toNum(v: string | number | undefined): number {
  const n = parseFloat(String(v ?? ""));
  return isNaN(n) ? 0 : n;
}

function scoreColor(score: string | number | undefined): string {
  const n = toNum(score);
  if (n === 0) return "#605E5C";
  if (n >= 75) return "#107C10";
  if (n >= 50) return "#FF8C00";
  return "#D13438";
}

function scoreBg(score: string | number | undefined): string {
  const n = toNum(score);
  if (n === 0) return "#F3F2F1";
  if (n >= 75) return "#DFF6DD";
  if (n >= 50) return "#FFF4CE";
  return "#FDE7E9";
}

function riskColor(level: string | undefined): string {
  const l = (level ?? "").toLowerCase();
  if (l.includes("low"))    return "#107C10";
  if (l.includes("medium")) return "#FF8C00";
  if (l.includes("high"))   return "#D13438";
  return "#605E5C";
}

function riskBg(level: string | undefined): string {
  const l = (level ?? "").toLowerCase();
  if (l.includes("low"))    return "#DFF6DD";
  if (l.includes("medium")) return "#FFF4CE";
  if (l.includes("high"))   return "#FDE7E9";
  return "#F3F2F1";
}

function dueDiligenceStatus(v: string | undefined): { icon: string; color: string; bg: string } {
  const s = (v ?? "").toLowerCase();
  if (s === "pass" || s === "validated" || s === "complete" || s === "yes")
    return { icon: "✓", color: "#107C10", bg: "#DFF6DD" };
  if (s === "fail" || s === "not validated" || s === "no")
    return { icon: "✕", color: "#D13438", bg: "#FDE7E9" };
  return { icon: "~", color: "#FF8C00", bg: "#FFF4CE" };
}

// ── Reusable Components ───────────────────────────────────────────────────────

function SectionCard({
  icon,
  title,
  badge,
  children,
}: {
  icon: string;
  title: string;
  badge?: string;
  children: React.ReactNode;
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200">
      <div className="flex items-center justify-between mb-5">
        <h2 className="text-xl font-bold text-[#323130] flex items-center gap-2">
          <span>{icon}</span>
          {title}
        </h2>
        {badge && (
          <span className="text-xs bg-[#E5F1FB] text-[#0078D4] px-3 py-1 rounded-full font-semibold">
            {badge}
          </span>
        )}
      </div>
      {children}
    </div>
  );
}

function KpiCard({
  icon,
  label,
  value,
  sub,
  accentColor,
  scoreValue,
  valueBg,
  valueColor,
}: {
  icon: string;
  label: string;
  value: string;
  sub?: string;
  accentColor: string;
  scoreValue?: number;
  valueBg?: string;
  valueColor?: string;
}) {
  return (
    <div
      className="bg-white rounded-xl shadow-sm border border-gray-200 p-5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200"
      style={{ borderTop: `4px solid ${accentColor}` }}
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xl">{icon}</span>
        <p className="text-xs uppercase tracking-wide text-[#605E5C] font-semibold">{label}</p>
      </div>
      <h2
        className="text-3xl font-bold leading-tight mt-1 px-2 py-0.5 rounded-lg inline-block"
        style={{
          color: valueColor ?? accentColor,
          backgroundColor: valueBg ?? "transparent",
        }}
      >
        {value}
      </h2>
      {sub && <p className="text-xs text-[#605E5C] mt-2">{sub}</p>}
      {scoreValue !== undefined && scoreValue > 0 && (
        <div className="mt-3">
          <div className="w-full bg-gray-100 rounded-full h-1.5">
            <div
              className="h-1.5 rounded-full transition-all duration-700"
              style={{
                width: `${Math.min(scoreValue, 100)}%`,
                backgroundColor: accentColor,
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
}

function TagList({
  items,
  emptyText,
  icon = "›",
  iconClass = "text-[#0078D4]",
}: {
  items: string[];
  emptyText: string;
  icon?: string;
  iconClass?: string;
}) {
  if (items.length === 0)
    return <p className="text-sm text-[#605E5C]">{emptyText}</p>;
  return (
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6">
          <span className={`shrink-0 font-bold mt-0.5 ${iconClass}`}>{icon}</span>
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}

function InfoRow({
  label,
  value,
  accentColor = "#0078D4",
}: {
  label: string;
  value: string;
  accentColor?: string;
}) {
  return (
    <div className="flex flex-col sm:flex-row sm:items-start gap-1 sm:gap-3 py-3 border-b border-gray-100 last:border-0">
      <span className="text-sm font-semibold sm:w-52 shrink-0" style={{ color: accentColor }}>
        {label}
      </span>
      <span className="text-[#323130] text-sm leading-6">{value}</span>
    </div>
  );
}

function ReadinessBar({
  label,
  value,
}: {
  label: string;
  value: string | number | undefined;
}) {
  const n = toNum(value);
  const hasScore = n > 0;
  return (
    <div className="space-y-1">
      <div className="flex justify-between items-center text-sm">
        <span className="text-[#323130] font-medium">{label}</span>
        <span className="font-bold" style={{ color: scoreColor(value) }}>
          {hasScore ? `${n}%` : val(value)}
        </span>
      </div>
      <div className="w-full bg-gray-100 rounded-full h-2">
        <div
          className="h-2 rounded-full transition-all duration-700"
          style={{
            width: `${hasScore ? Math.min(n, 100) : 0}%`,
            backgroundColor: scoreColor(value),
          }}
        />
      </div>
    </div>
  );
}

// ── Circular Score Ring ───────────────────────────────────────────────────────

function ScoreRing({
  score,
  label,
}: {
  score: string | number | undefined;
  label: string;
}) {
  const n = Math.min(toNum(score), 100);
  const radius = 52;
  const circ = 2 * Math.PI * radius;
  const offset = circ - (n / 100) * circ;
  const color = scoreColor(score);

  return (
    <div className="flex flex-col items-center gap-2">
      <div className="relative w-32 h-32">
        <svg className="w-32 h-32 -rotate-90" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r={radius} fill="none" stroke="#E5E5E5" strokeWidth="10" />
          <circle
            cx="60"
            cy="60"
            r={radius}
            fill="none"
            stroke={color}
            strokeWidth="10"
            strokeDasharray={circ}
            strokeDashoffset={offset}
            strokeLinecap="round"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-3xl font-bold" style={{ color }}>
            {n > 0 ? n : "—"}
          </span>
          {n > 0 && <span className="text-xs text-[#605E5C]">/100</span>}
        </div>
      </div>
      <p className="text-sm font-semibold text-[#323130] text-center">{label}</p>
    </div>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function InvestorReadiness({ report }: Props) {

  if (!report) {
    return (
      <div className="flex flex-col items-center justify-center h-[60vh] gap-3">
        <span className="text-5xl">💰</span>
        <p className="text-[#605E5C] text-lg font-medium">No investor data available.</p>
        <p className="text-sm text-gray-400">Run an analysis to see investor readiness insights.</p>
      </div>
    );
  }

  const investor = report.investor ?? {};
  const metadata = report.metadata ?? {};

  const strengths            = arr(investor.strengths);
  const competitiveAdvantages = arr(investor.competitive_advantages);
  const strongestPoints      = arr(investor.strongest_points);
  const risks                = arr(investor.risks);
  const operationalRisks     = arr(investor.operational_risks);
  const marketRisks          = arr(investor.market_risks);
  const financialRisks       = arr(investor.financial_risks);
  const technologyRisks      = arr(investor.technology_risks);
  const investmentConcerns   = arr(investor.investment_concerns);
  const suggestedImprovements = arr(investor.suggested_improvements);
  const useOfFunds           = arr(investor.use_of_funds);
  const topRecommendations   = arr(investor.top_recommendations);
  const improvementsBeforeFundraising = arr(investor.improvements_before_fundraising);
  const nextMilestones       = arr(investor.next_milestones);
  const growthPriorities     = arr(investor.growth_priorities);

  const raisedLabel = investor.recommended_raise ?? investor.raise_amount;

  const shouldInvestRaw = investor.should_invest;
  const shouldInvestStr =
    shouldInvestRaw === true || String(shouldInvestRaw).toLowerCase() === "yes"
      ? "Yes"
      : shouldInvestRaw === false || String(shouldInvestRaw).toLowerCase() === "no"
      ? "No"
      : val(shouldInvestRaw as string, "Under Review");

  const dd = investor.due_diligence ?? {};
  const ddChecklist = [
    { label: "Product Validation",  status: dd.product_validation },
    { label: "Market Validation",   status: dd.market_validation },
    { label: "Revenue Validation",  status: dd.revenue_validation },
    { label: "Team Validation",     status: dd.team_validation },
    { label: "Financial Validation",status: dd.financial_validation },
  ];

  const generatedAt = metadata.generated_at
    ? new Date(metadata.generated_at).toLocaleString("en-US", { dateStyle: "medium", timeStyle: "short" })
    : null;

  return (
    <div className="space-y-8 text-gray-700">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-[#323130]">Investor Readiness</h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-generated investor intelligence ·{" "}
            <span className="text-[#0078D4] font-medium">Investor Readiness Agent</span>
          </p>
          {generatedAt && (
            <p className="text-xs text-[#605E5C] mt-1">🕐 Generated: {generatedAt}</p>
          )}
        </div>
        <div className="flex flex-col gap-2 items-start sm:items-end">
          <span className="bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
            ✦ Microsoft Azure AI Foundry
          </span>
          <span className="bg-[#DFF6DD] text-[#107C10] px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
            ✓ AI-Generated Analysis
          </span>
        </div>
      </div>

      {/* ── Score Rings + Decision Banner ── */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200">
        <div className="flex flex-col lg:flex-row items-center gap-8">

          {/* Score Rings */}
          <div className="flex flex-wrap justify-center gap-10">
            <ScoreRing score={investor.readiness_score}  label="Investment Readiness" />
            <ScoreRing score={investor.overall_score}    label="Overall Startup Score" />
            <ScoreRing score={investor.ai_confidence}    label="AI Confidence" />
          </div>

          {/* Decision Card */}
          <div className="flex-1 w-full space-y-4">

            {/* Should Invest? */}
            <div
              className="rounded-xl p-5 border-l-4 flex items-center gap-4"
              style={{
                borderColor: shouldInvestStr === "Yes" ? "#107C10" : shouldInvestStr === "No" ? "#D13438" : "#FF8C00",
                backgroundColor: shouldInvestStr === "Yes" ? "#DFF6DD" : shouldInvestStr === "No" ? "#FDE7E9" : "#FFF4CE",
              }}
            >
              <span className="text-4xl">
                {shouldInvestStr === "Yes" ? "✅" : shouldInvestStr === "No" ? "❌" : "🟡"}
              </span>
              <div>
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide">
                  AI Investment Decision
                </p>
                <p
                  className="text-2xl font-bold"
                  style={{
                    color: shouldInvestStr === "Yes" ? "#107C10" : shouldInvestStr === "No" ? "#D13438" : "#FF8C00",
                  }}
                >
                  {shouldInvestStr}
                </p>
              </div>
            </div>

            {/* Outlook + Risk side by side */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div className="bg-[#F3F2F1] rounded-xl p-4">
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">Investment Outlook</p>
                <p className="text-lg font-bold text-[#0078D4]">{val(investor.investment_outlook)}</p>
              </div>
              <div
                className="rounded-xl p-4"
                style={{ backgroundColor: riskBg(investor.risk_level) }}
              >
                <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">Risk Level</p>
                <p
                  className="text-lg font-bold"
                  style={{ color: riskColor(investor.risk_level) }}
                >
                  {val(investor.risk_level)}
                </p>
              </div>
            </div>

          </div>
        </div>
      </div>

      {/* ── KPI Cards ── */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-5">
        <KpiCard
          icon="🎯"
          label="Overall Score"
          value={val(investor.overall_score)}
          sub="Startup health"
          accentColor={scoreColor(investor.overall_score)}
          scoreValue={toNum(investor.overall_score)}
          valueColor={scoreColor(investor.overall_score)}
          valueBg={scoreBg(investor.overall_score)}
        />
        <KpiCard
          icon="💡"
          label="Readiness Score"
          value={val(investor.readiness_score)}
          sub="Out of 100"
          accentColor={scoreColor(investor.readiness_score)}
          scoreValue={toNum(investor.readiness_score)}
          valueColor={scoreColor(investor.readiness_score)}
          valueBg={scoreBg(investor.readiness_score)}
        />
        <KpiCard
          icon="🏦"
          label="Funding Stage"
          value={val(investor.funding_stage)}
          sub="Recommended"
          accentColor="#0078D4"
        />
        <KpiCard
          icon="💰"
          label="Raise Amount"
          value={val(raisedLabel)}
          sub="Target raise"
          accentColor="#107C10"
        />
        <KpiCard
          icon="🤖"
          label="AI Confidence"
          value={investor.ai_confidence ? `${investor.ai_confidence}%` : "N/A"}
          sub="Model confidence"
          accentColor="#8764B8"
          scoreValue={toNum(investor.ai_confidence)}
        />
        <KpiCard
          icon="⚠️"
          label="Risk Level"
          value={val(investor.risk_level)}
          sub="Investment risk"
          accentColor={riskColor(investor.risk_level)}
          valueColor={riskColor(investor.risk_level)}
          valueBg={riskBg(investor.risk_level)}
        />
      </div>

      {/* ── Funding Analysis ── */}
      <SectionCard icon="🏦" title="Funding Analysis">
        <div className="space-y-0">
          <InfoRow label="Funding Stage"       value={val(investor.funding_stage)} />
          <InfoRow label="Capital Requirement" value={val(investor.capital_requirement)} />
          <InfoRow label="Recommended Raise"   value={val(raisedLabel)} accentColor="#107C10" />
          <InfoRow label="Runway Estimate"      value={val(investor.runway_estimate)} />
          {investor.valuation_estimate && (
            <InfoRow label="Valuation Estimate" value={investor.valuation_estimate} accentColor="#8764B8" />
          )}
        </div>
        {useOfFunds.length > 0 && (
          <div className="mt-5">
            <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-3">Use of Funds</p>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {useOfFunds.map((item, i) => (
                <div key={i} className="flex items-start gap-2 bg-[#F3F2F1] rounded-lg px-3 py-2 text-sm text-[#323130]">
                  <span className="text-[#0078D4] font-bold shrink-0">💼</span>
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </SectionCard>

      {/* ── Investment Metrics ── */}
      <SectionCard icon="📊" title="Investment Metrics">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {[
            { label: "Market Potential",  value: investor.market_potential },
            { label: "Revenue Potential", value: investor.revenue_potential },
            { label: "Scalability",       value: investor.scalability },
            { label: "Traction",          value: investor.traction },
            { label: "Business Maturity", value: investor.business_maturity },
          ].map((item) => (
            <div key={item.label} className="bg-[#F3F2F1] rounded-xl p-4 hover:bg-[#E5F1FB] transition-colors duration-200">
              <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide mb-1">{item.label}</p>
              <p className="text-sm font-bold text-[#323130] leading-5">{val(item.value)}</p>
            </div>
          ))}
        </div>
      </SectionCard>

      {/* ── Investor Strengths ── */}
      <SectionCard icon="💪" title="Investor Strengths">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div>
            <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-3">Investment Strengths</p>
            <TagList items={strengths} emptyText="No strengths listed." icon="✅" iconClass="text-[#107C10]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-3">Competitive Advantages</p>
            <TagList items={competitiveAdvantages} emptyText="No advantages listed." icon="⭐" iconClass="text-[#0078D4]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#8764B8] uppercase tracking-wide mb-3">Strongest Points</p>
            <TagList items={strongestPoints} emptyText="No points listed." icon="🏆" iconClass="text-[#8764B8]" />
          </div>
        </div>
      </SectionCard>

      {/* ── Investment Risks ── */}
      <SectionCard icon="⚠️" title="Investment Risks">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div>
            <p className="text-xs font-semibold text-[#D13438] uppercase tracking-wide mb-3">Key Risks</p>
            <TagList items={risks} emptyText="No risks listed." icon="🔴" iconClass="text-[#D13438]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#FF8C00] uppercase tracking-wide mb-3">Operational Risks</p>
            <TagList items={operationalRisks} emptyText="None identified." icon="⚙️" iconClass="text-[#FF8C00]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#D13438] uppercase tracking-wide mb-3">Market Risks</p>
            <TagList items={marketRisks} emptyText="None identified." icon="📉" iconClass="text-[#D13438]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#FF8C00] uppercase tracking-wide mb-3">Financial Risks</p>
            <TagList items={financialRisks} emptyText="None identified." icon="💸" iconClass="text-[#FF8C00]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#8764B8] uppercase tracking-wide mb-3">Technology Risks</p>
            <TagList items={technologyRisks} emptyText="None identified." icon="🖥️" iconClass="text-[#8764B8]" />
          </div>
        </div>
      </SectionCard>

      {/* ── AI Investment Recommendation ── */}
      <SectionCard icon="🤖" title="AI Investment Recommendation">
        <div className="space-y-0 mb-5">
          <InfoRow label="AI Recommendation"   value={val(investor.recommendation, "No recommendation available.")} />
          <InfoRow label="Investment Thesis"    value={val(investor.investment_thesis, "No thesis available.")} accentColor="#107C10" />
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
          <div>
            <p className="text-xs font-semibold text-[#D13438] uppercase tracking-wide mb-3">Investment Concerns</p>
            <TagList items={investmentConcerns} emptyText="No concerns identified." icon="⚠️" iconClass="text-[#D13438]" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-3">Suggested Improvements</p>
            <TagList items={suggestedImprovements} emptyText="No suggestions available." icon="✓" iconClass="text-[#107C10]" />
          </div>
        </div>
      </SectionCard>

      {/* ── Due Diligence Checklist ── */}
      <SectionCard icon="📋" title="Due Diligence Checklist">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3">
          {ddChecklist.map((item) => {
            const s = dueDiligenceStatus(item.status);
            return (
              <div
                key={item.label}
                className="rounded-xl p-4 flex flex-col items-center gap-2 text-center border border-gray-200 hover:shadow-sm transition-all"
                style={{ backgroundColor: s.bg }}
              >
                <span
                  className="w-9 h-9 rounded-full flex items-center justify-center text-base font-bold"
                  style={{ color: s.color, backgroundColor: "white" }}
                >
                  {s.icon}
                </span>
                <p className="text-xs font-semibold text-[#323130]">{item.label}</p>
                <span
                  className="text-xs font-medium px-2 py-0.5 rounded-full"
                  style={{ color: s.color, backgroundColor: "white" }}
                >
                  {val(item.status, "Pending")}
                </span>
              </div>
            );
          })}
        </div>
      </SectionCard>

      {/* ── Funding Readiness Bars ── */}
      <SectionCard icon="📈" title="Funding Readiness">
        <div className="space-y-4">
          <ReadinessBar label="Fundraising Readiness" value={investor.fundraising_readiness} />
          <ReadinessBar label="Pitch Readiness"       value={investor.pitch_readiness} />
          <ReadinessBar label="Business Readiness"    value={investor.business_readiness} />
          <ReadinessBar label="Market Readiness"      value={investor.market_readiness} />
          <ReadinessBar label="Technology Readiness"  value={investor.technology_readiness} />
        </div>
      </SectionCard>

      {/* ── AI Recommendations ── */}
      <SectionCard icon="🧠" title="AI Recommendations">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {topRecommendations.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-3">Top Recommendations</p>
              <ol className="space-y-2">
                {topRecommendations.map((r, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6 bg-[#F3F2F1] rounded-lg px-4 py-2">
                    <span className="shrink-0 font-bold text-[#0078D4]">{i + 1}.</span>
                    <span>{r}</span>
                  </li>
                ))}
              </ol>
            </div>
          )}

          {improvementsBeforeFundraising.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-[#FF8C00] uppercase tracking-wide mb-3">Before Fundraising</p>
              <TagList items={improvementsBeforeFundraising} emptyText="None listed." icon="🔧" iconClass="text-[#FF8C00]" />
            </div>
          )}

          {nextMilestones.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-[#8764B8] uppercase tracking-wide mb-3">Next Milestones</p>
              <TagList items={nextMilestones} emptyText="None listed." icon="🎯" iconClass="text-[#8764B8]" />
            </div>
          )}

          {growthPriorities.length > 0 && (
            <div>
              <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-3">Growth Priorities</p>
              <TagList items={growthPriorities} emptyText="None listed." icon="🚀" iconClass="text-[#107C10]" />
            </div>
          )}

          {topRecommendations.length === 0 &&
           improvementsBeforeFundraising.length === 0 &&
           nextMilestones.length === 0 &&
           growthPriorities.length === 0 && (
            <div className="md:col-span-2">
              <p className="text-sm text-[#605E5C]">No AI recommendations available.</p>
            </div>
          )}

        </div>
      </SectionCard>

      {/* ── Footer Branding ── */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
        <p className="text-xs text-[#605E5C]">
          Powered by{" "}
          <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
          · Investor Readiness Agent
        </p>
        {generatedAt && (
          <p className="text-xs text-[#605E5C]">Report generated: {generatedAt}</p>
        )}
      </div>

    </div>
  );
}
