// ── TypeScript Interfaces ──────────────────────────────────────────────────────

interface Competitor {
  name: string;
  strength?: string;
}

interface AgentExecution {
  agent: string;
  status: string;
  execution_time?: number;
}

interface MarketData {
  market_size?: string;
  growth_rate?: string;
  tam?: string;
  sam?: string;
  som?: string;
  competitors?: Competitor[];
}

interface InvestorData {
  readiness_score?: string | number;
  funding_stage?: string;
  recommended_raise?: string;
  raise_amount?: string;
  investment_outlook?: string;
}

interface ReportMetadata {
  generated_at?: string;
  analysis_time?: string | number;
}

interface Report {
  market?: MarketData;
  investor?: InvestorData;

  execution_log?: AgentExecution[];

  metadata?: ReportMetadata;

  recommendations?: string[];

  analysis_summary?: {
    overall_score?: number;
    investment_outlook?: string;
    agents_completed?: number;
    total_agents?: number;
  };

  executive_summary?: {
    ai_insight?: string;
  };

  swot?: {
    strengths?: string[];
    weaknesses?: string[];
    opportunities?: string[];
    risks?: string[];
    threats?: string[];
  };
}

interface Props {
  report: Report | null;
}


// ── Helpers ───────────────────────────────────────────────────────────────────

function val(v: string | number | undefined, fallback = "N/A"): string {
  if (v === undefined || v === null || v === "") return fallback;
  return String(v);
}

function scoreColor(score: string | number | undefined): string {
  const n = parseFloat(String(score));
  if (isNaN(n)) return "#0078D4";
  if (n >= 75) return "#107C10";
  if (n >= 50) return "#FF8C00";
  return "#D13438";
}

function scoreBg(score: string | number | undefined): string {
  const n = parseFloat(String(score));
  if (isNaN(n)) return "#E5F1FB";
  if (n >= 75) return "#DFF6DD";
  if (n >= 50) return "#FFF4CE";
  return "#FDE7E9";
}

function agentStatusColor(status: string): string {
  if (status === "Completed") return "#107C10";
  if (status === "Failed") return "#D13438";
  return "#0078D4";
}

function agentStatusBg(status: string): string {
  if (status === "Completed") return "#DFF6DD";
  if (status === "Failed") return "#FDE7E9";
  return "#E5F1FB";
}

function agentStatusIcon(status: string): string {
  if (status === "Completed") return "✓";
  if (status === "Failed") return "✕";
  return "⟳";
}

// ── Sub-components ────────────────────────────────────────────────────────────

function SectionCard({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div
      className={`bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200 ${className}`}
    >
      {children}
    </div>
  );
}

function SectionHeading({
  icon,
  title,
  badge,
}: {
  icon: string;
  title: string;
  badge?: string;
}) {
  return (
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
  );
}

function KpiCard({
  icon,
  label,
  value,
  sub,
  accentColor,
  scoreValue,
}: {
  icon: string;
  label: string;
  value: string;
  sub?: string;
  accentColor: string;
  scoreValue?: string | number;
}) {
  return (
    <div
      className="bg-white rounded-xl shadow-sm border border-gray-200 p-5 hover:shadow-md hover:-translate-y-1 transition-all duration-200"
      style={{ borderTop: `4px solid ${accentColor}` }}
    >
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xl">{icon}</span>
        <p className="text-xs uppercase tracking-wide text-[#605E5C] font-semibold">
          {label}
        </p>
      </div>
      <h2 className="text-3xl font-bold text-[#323130] leading-tight mt-1">
        {value}
      </h2>
      {sub && (
        <p className="text-xs text-[#605E5C] mt-2">{sub}</p>
      )}
      {scoreValue !== undefined && (
        <div className="mt-3">
          <div className="w-full bg-gray-100 rounded-full h-1.5">
            <div
              className="h-1.5 rounded-full transition-all duration-500"
              style={{
                width: `${Math.min(parseFloat(String(scoreValue)) || 0, 100)}%`,
                backgroundColor: accentColor,
              }}
            />
          </div>
        </div>
      )}
    </div>
  );
}

function OverviewRow({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="flex flex-col sm:flex-row sm:items-start gap-1 sm:gap-3 py-3 border-b border-gray-100 last:border-0">
      <span className="text-sm font-semibold text-[#0078D4] sm:w-44 shrink-0">
        {label}
      </span>
      <span className="text-[#323130] text-sm leading-6">{value}</span>
    </div>
  );
}

function InsightList({
  items,
  icon,
  emptyText,
}: {
  items: string[];
  icon: string;
  emptyText: string;
}) {
  if (!items || items.length === 0) {
    return <p className="text-sm text-[#605E5C]">{emptyText}</p>;
  }
  return (
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6">
          <span className="mt-0.5 shrink-0 text-base">{icon}</span>
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function Dashboard({ report }: Props) {

  if (!report) {
    return (
      <div className="flex flex-col items-center justify-center h-[60vh] gap-3">
        <span className="text-5xl">🚀</span>
        <p className="text-[#605E5C] text-lg font-medium">Run an analysis to see your dashboard.</p>
        <p className="text-sm text-gray-400">Enter your startup details and click Analyze.</p>
      </div>
    );
  }

  const market    = report.market ?? {};
  const investor  = report.investor ?? {};
  const swot  = report.swot ?? {};
  const metadata  = report.metadata ?? {};
  const agents: AgentExecution[] = Array.isArray(report.execution_log)? report.execution_log: [];
  const recommendations: string[] = Array.isArray(report.recommendations) ? report.recommendations : [];

  const competitors = Array.isArray(market.competitors) ? market.competitors : [];
  const strengths = Array.isArray(swot.strengths) ? swot.strengths: [];

  const risks = Array.isArray(swot.risks) ? swot.risks: [];  

  const opportunities = Array.isArray(swot.opportunities)? swot.opportunities: [];

  const completedAgents = report.analysis_summary?.agents_completed ?? agents.filter(a => a.status === "Completed").length;
  const totalAgents = report.analysis_summary?.total_agents ?? agents.length ?? 12;
  const generatedAt = metadata.generated_at ?? "Not Available"
    ? new Date(metadata.generated_at).toLocaleString("en-US", {
        dateStyle: "medium",
        timeStyle: "short",
      })
    : null;

  const analysisTime = metadata.analysis_time
    ? `${metadata.analysis_time}s`
    : null;

  return (
    <div className="space-y-8 text-gray-700">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-[#323130]">Dashboard</h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-powered Startup Intelligence · Analyzed by{" "}
            <span className="font-medium text-[#0078D4]">12 Specialized AI Agents</span>
          </p>
          <div className="flex flex-wrap gap-3 mt-2">
            {generatedAt && (
              <span className="text-xs text-[#605E5C]">
                🕐 Generated: {generatedAt}
              </span>
            )}
            {analysisTime && (
              <span className="text-xs text-[#605E5C]">
                ⚡ Analysis time: {analysisTime}
              </span>
            )}
          </div>
        </div>
        <div className="flex flex-col gap-2 items-start sm:items-end">
          <span className="bg-[#E5F1FB] text-[#0078D4] px-4 py-2 rounded-full text-sm font-semibold whitespace-nowrap">
            ✦ Powered by Microsoft Azure AI Foundry
          </span>
          <span className="bg-[#DFF6DD] text-[#107C10] px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
            ✓ {completedAgents}/{totalAgents} Agents Completed
          </span>
        </div>
      </div>

      {/* ── AI Insight Banner ── */}
      <div className="bg-[#E5F1FB] border-l-4 border-[#0078D4] p-5 rounded-xl">
        <h3 className="font-semibold text-[#0078D4] text-base flex items-center gap-2">
          <span>🤖</span> AI Insight
        </h3>
        <p className="text-[#323130] mt-1 text-sm leading-6">
          {report.executive_summary?.ai_insight || "Startup analysis completed successfully. Scroll down to explore detailed insights across market, competitor, and investor dimensions."}
        </p>
      </div>

      {/* ── KPI Cards ── */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">

        <KpiCard
          icon="📊"
          label="Market Size"
          value={val(market.market_size?.split("(")[0]?.trim())}
          sub="Total addressable opportunity"
          accentColor="#0078D4"
        />

        <KpiCard
          icon="📈"
          label="Growth Rate"
          value={val(market.growth_rate)}
          sub="CAGR"
          accentColor="#107C10"
        />

        <KpiCard
          icon="💡"
          label="Investment Readiness"
          value={val(investor.readiness_score)}
          sub="Out of 100"
          accentColor="#8764B8"
          scoreValue={investor.readiness_score}
        />

        <KpiCard
          icon="🏢"
          label="Competitors"
          value={String(competitors.length || 0)}
          sub="Identified by AI"
          accentColor="#F7630C"
        />

        <KpiCard
          icon="🎯"
          label="Overall Score"
          value={String(report.analysis_summary?.overall_score ?? "N/A")}
          sub="Startup health score"
          accentColor={scoreColor(report.analysis_summary?.overall_score)}
          scoreValue={report.analysis_summary?.overall_score}
        />

        <KpiCard
          icon="🤖"
          label="AI Confidence"
          value={`${Math.round((completedAgents / totalAgents) * 100)}%`}
          sub="Model confidence level"
          accentColor="#0078D4"
          scoreValue={Math.round((completedAgents / totalAgents) * 100)}
        />

        <KpiCard
          icon="💰"
          label="Funding Stage"
          value={val(investor.funding_stage)}
          sub="Recommended stage"
          accentColor="#107C10"
        />

        <KpiCard
          icon="🔮"
          label="Investment Outlook"
          value={
            report.analysis_summary?.investment_outlook ||
            "N/A"
          }
          sub="AI assessment"
          accentColor="#8764B8"
        />

      </div>

      {/* ── Executive Summary + Business Overview ── */}
      <SectionCard>
        <SectionHeading icon="📋" title="Executive Summary" />
        <div className="space-y-0">
          <OverviewRow
              label="Executive Summary"
              value={report.executive_summary?.ai_insight || "No executive summary available."}
          />

          <OverviewRow
              label="Business Model"
              value={
                report.executive_summary?.executive_summary ||
                "No executive summary available."
              }
          />

          <OverviewRow
              label="Target Customer"
              value={
                report.executive_summary?.target_customer ||
                "Not specified."
              }
          />
          <OverviewRow
            label="Funding Recommendation"
            value={
              investor.recommended_raise ??
              investor.raise_amount ??
              investor.funding_stage ??
              "Not available"
            }
          />
          <OverviewRow
            label="Market Size"
            value={val(market.market_size)}
          />
          <OverviewRow
            label="Growth Rate"
            value={val(market.growth_rate)}
          />
          <OverviewRow
            label="Investment Readiness"
            value={String(investor.readiness_score ?? 0)}
          />
          <OverviewRow
            label="Competitors"
            value={
              competitors.length > 0
                ? competitors.map((c) => c.name).join(", ")
                : "None identified"
            }
          />
        </div>
      </SectionCard>

      {/* ── AI Insights: Strengths / Risks / Opportunities ── */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">

        <SectionCard>
          <SectionHeading icon="💪" title="Strengths" />
          <InsightList
            items={strengths}
            icon="✅"
            emptyText="No strengths identified."
          />
        </SectionCard>

        <SectionCard>
          <SectionHeading icon="⚠️" title="Major Risks" />
          <InsightList
            items={risks}
            icon="🔴"
            emptyText="No risks identified."
          />
        </SectionCard>

        <SectionCard>
          <SectionHeading icon="🚀" title="Growth Opportunities" />
          <InsightList
            items={opportunities}
            icon="🟢"
            emptyText="No opportunities identified."
          />
        </SectionCard>

      </div>

      {/* ── AI Recommendations ── */}
      {recommendations.length > 0 && (
        <SectionCard>
          <SectionHeading icon="🧠" title="AI Recommendations" />
          <ul className="space-y-3">
            {recommendations.map((rec, i) => (
              <li
                key={i}
                className="flex items-start gap-3 bg-[#F3F2F1] rounded-lg p-4 text-sm text-[#323130] leading-6"
              >
                <span className="shrink-0 font-bold text-[#0078D4]">{i + 1}.</span>
                <span>{rec}</span>
              </li>
            ))}
          </ul>
        </SectionCard>
      )}

      {/* ── Market Snapshot ── */}
      <SectionCard>
        <SectionHeading icon="🌍" title="Market Snapshot" />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            { label: "TAM", value: val(market.tam), desc: "Total Addressable Market" },
            { label: "SAM", value: val(market.sam), desc: "Serviceable Available Market" },
            { label: "SOM", value: val(market.som), desc: "Serviceable Obtainable Market" },
            { label: "Growth Rate", value: val(market.growth_rate), desc: "CAGR" },
          ].map((item) => (
            <div
              key={item.label}
              className="bg-[#F3F2F1] rounded-xl p-4 hover:bg-[#E5F1FB] transition-colors duration-200"
            >
              <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide">
                {item.label}
              </p>
              <p className="text-2xl font-bold text-[#323130] mt-1">{item.value}</p>
              <p className="text-xs text-[#605E5C] mt-1">{item.desc}</p>
            </div>
          ))}
        </div>
      </SectionCard>

      {/* ── Competitor Snapshot ── */}
      <SectionCard>
        <SectionHeading
          icon="🏢"
          title="Competitor Snapshot"
          badge={competitors.length > 0 ? `${competitors.length} identified` : undefined}
        />
        {competitors.length > 0 ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {competitors.map((c, i) => (
              <div
                key={i}
                className="bg-[#F3F2F1] border border-gray-200 rounded-xl p-4 hover:border-[#0078D4] hover:shadow-sm transition-all duration-200"
              >
                <div className="flex items-center gap-2 mb-2">
                  <span className="w-6 h-6 rounded-full bg-[#0078D4] text-white text-xs font-bold flex items-center justify-center shrink-0">
                    {i + 1}
                  </span>
                  <p className="font-semibold text-[#0078D4] text-sm">{c.name}</p>
                </div>
                {c.strength && (
                  <p className="text-xs text-[#605E5C] leading-5 pl-8">{c.strength}</p>
                )}
              </div>
            ))}
          </div>
        ) : (
          <p className="text-sm text-[#605E5C]">No competitors identified.</p>
        )}
      </SectionCard>

      {/* ── Investor Snapshot ── */}
      <SectionCard>
        <SectionHeading icon="💰" title="Investor Snapshot" />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            { label: "Funding Stage", value: val(investor.funding_stage) },
            { label: "Raise Amount", value: val(investor.raise_amount) },
            { label: "Readiness Score", value: val(investor.readiness_score) },
            { label: "Investment Outlook", value: val(investor.investment_outlook) },
          ].map((item) => (
            <div
              key={item.label}
              className="bg-[#F3F2F1] rounded-xl p-4 hover:bg-[#E5F1FB] transition-colors duration-200"
            >
              <p className="text-xs font-semibold text-[#605E5C] uppercase tracking-wide">
                {item.label}
              </p>
              <p className="text-xl font-bold text-[#323130] mt-1 leading-tight">
                {item.value}
              </p>
            </div>
          ))}
        </div>
        {/* Investment Readiness Progress */}
        {investor.readiness_score !== undefined && (
          <div className="mt-5">
            <div className="flex justify-between text-xs text-[#605E5C] mb-1">
              <span>Investment Readiness</span>
              <span>{investor.readiness_score}/100</span>
            </div>
            <div className="w-full bg-gray-100 rounded-full h-2">
              <div
                className="h-2 rounded-full transition-all duration-700"
                style={{
                  width: `${Math.min(parseFloat(String(investor.readiness_score)) || 0, 10)}%`,
                  backgroundColor: scoreColor(investor.readiness_score),
                }}
              />
            </div>
          </div>
        )}
      </SectionCard>

      {/* ── Multi-Agent Execution ── */}
      {agents.length > 0 && (
        <SectionCard>
          <SectionHeading
            icon="⚙️"
            title="Multi-Agent Execution"
            badge={`${completedAgents}/${agents.length} Completed`}
          />
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {agents.map((agent, i) => (
              <div
                key={i}
                className="flex items-center justify-between bg-[#F3F2F1] rounded-xl px-4 py-3 border border-gray-200"
              >
                <div className="flex items-center gap-2">
                  <span
                    className="w-6 h-6 rounded-full text-xs font-bold flex items-center justify-center shrink-0"
                    style={{
                      backgroundColor: agentStatusBg(agent.status),
                      color: agentStatusColor(agent.status),
                    }}
                  >
                    {agentStatusIcon(agent.status)}
                  </span>
                  <span className="text-sm font-medium text-[#323130]">
                    {agent.agent}
                  </span>
                </div>
                {agent.execution_time !== undefined && (
                  <span className="text-xs text-[#605E5C] whitespace-nowrap ml-2">
                    {agent.execution_time}s
                  </span>
                )}
              </div>
            ))}
          </div>
          {/* Execution Timeline Bar */}
          <div className="mt-5">
            <div className="flex justify-between text-xs text-[#605E5C] mb-1">
              <span>Execution Progress</span>
              <span>{Math.round((completedAgents / (agents.length || 1)) * 100)}%</span>
            </div>
            <div className="w-full bg-gray-100 rounded-full h-2">
              <div
                className="h-2 rounded-full bg-[#107C10] transition-all duration-700"
                style={{
                  width: `${Math.round((completedAgents / (agents.length || 1)) * 100)}%`,
                }}
              />
            </div>
          </div>
        </SectionCard>
      )}

      {/* ── Footer Branding ── */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
        <p className="text-xs text-[#605E5C]">
          Powered by{" "}
          <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
          · 12 Specialized AI Agents
        </p>
        {generatedAt && (
          <p className="text-xs text-[#605E5C]">Report generated: {generatedAt}</p>
        )}
      </div>

    </div>
  );
}
