"use client";

import React from "react";

// ── TypeScript Interfaces ──────────────────────────────────────────────────────

interface BusinessData {
  // Overview
  business_model?: string;
  startup_vision?: string;
  mission_statement?: string;
  acquisition_channels?: string[];
  value_proposition?: string;
  usp?: string;

  // Customer
  target_customer?: string;
  customer_segments?: string[];
  customer_pain_points?: string[];
  customer_personas?: string[];

  // Revenue
  revenue_model?: string;
  revenue_streams?: string[];
  pricing_strategy?: string;
  monetization_strategy?: string;
  expected_revenue_growth?: string;

  // Go-To-Market
  go_to_market?: string;
  marketing_channels?: string[];
  sales_strategy?: string;
  distribution_channels?: string[];
  partnership_strategy?: string;

  // Growth
  growth_roadmap?: string[];
  expansion_strategy?: string;
  scaling_plan?: string;
  market_expansion?: string;
  international_expansion?: string;

  // Competitive Advantage
  key_advantages?: string[];
  competitive_differentiators?: string[];
  innovation_strategy?: string;
  ai_advantage?: string;
  technology_advantage?: string;

  executive_summary?: string;
}

interface SwotData {
  strengths?: string[];
  weaknesses?: string[];
  opportunities?: string[];
  threats?: string[];
}

interface Props {
  report: {
    business?: BusinessData;
    investor?: {
      recommendations?: string[];
    };
    swot?: SwotData;
    executive_summary?: {
      executive_summary?: string;
    };
    metadata?: {
      generated_at?: string;
    };
  } | null;
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function val(v: string | number | undefined, fallback = "Not available"): string {
  return (v !== undefined && v !== null && String(v).trim() !== "")
    ? String(v)
    : fallback;
}

function arr(v: string[] | undefined): string[] {
  return Array.isArray(v) ? v : [];
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

function InfoCard({
  label,
  value,
  accent = "#0078D4",
}: {
  label: string;
  value: string;
  accent?: string;
}) {
  return (
    <div className="bg-[#F3F2F1] rounded-xl p-4 hover:shadow-sm hover:bg-[#EBF3FB] transition-all duration-200">
      <p
        className="text-xs font-semibold uppercase tracking-wide mb-1"
        style={{ color: accent }}
      >
        {label}
      </p>
      <p className="text-[#323130] text-sm leading-6">{value}</p>
    </div>
  );
}

function MetricCard({
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
      className="bg-white rounded-xl shadow-sm border border-gray-200 p-5 hover:shadow-md hover:-translate-y-0.5 transition-all duration-200"
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
      {sub && <p className="text-xs text-[#605E5C] mt-2">{sub}</p>}
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

function TagList({
  items,
  emptyText,
  icon = "›",
  colorClass = "text-[#0078D4]",
}: {
  items: string[];
  emptyText: string;
  icon?: string;
  colorClass?: string;
}) {
  if (items.length === 0) {
    return <p className="text-sm text-[#605E5C]">{emptyText}</p>;
  }
  return (
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li
          key={i}
          className="flex items-start gap-2 text-sm text-[#323130] leading-6"
        >
          <span className={`shrink-0 font-bold mt-0.5 ${colorClass}`}>
            {icon}
          </span>
          <span>{item}</span>
        </li>
      ))}
    </ul>
  );
}

function SwotQuadrant({
  icon,
  label,
  items,
  borderColor,
  bgColor,
  iconColor,
}: {
  icon: string;
  label: string;
  items: string[];
  borderColor: string;
  bgColor: string;
  iconColor: string;
}) {
  return (
    <div
      className="rounded-xl p-5 border-l-4"
      style={{ borderColor, backgroundColor: bgColor }}
    >
      <h3
        className="font-bold text-sm uppercase tracking-wide mb-3 flex items-center gap-1"
        style={{ color: borderColor }}
      >
        <span>{icon}</span> {label}
      </h3>
      {items.length > 0 ? (
        <ul className="space-y-2">
          {items.map((item, i) => (
            <li
              key={i}
              className="flex items-start gap-2 text-sm text-[#323130] leading-5"
            >
              <span className="shrink-0 font-bold" style={{ color: iconColor }}>
                •
              </span>
              <span>{item}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-sm text-[#605E5C]">None identified.</p>
      )}
    </div>
  );
}

function RoadmapTimeline({ steps }: { steps: string[] }) {
  if (steps.length === 0) {
    return <p className="text-sm text-[#605E5C]">No roadmap data available.</p>;
  }
  return (
    <ol className="relative border-l-2 border-[#0078D4] ml-3 space-y-5">
      {steps.map((step, i) => (
        <li key={i} className="ml-5">
          <span className="absolute -left-3 flex items-center justify-center w-6 h-6 rounded-full bg-[#0078D4] text-white text-xs font-bold">
            {i + 1}
          </span>
          <p className="text-sm text-[#323130] leading-6 bg-[#F3F2F1] rounded-lg px-4 py-2">
            {step}
          </p>
        </li>
      ))}
    </ol>
  );
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function BusinessStrategy({ report }: Props) {

  console.log("BUSINESS REPORT");
  console.log(report?.business);

  if (!report) {
    return (
      <div className="flex flex-col items-center justify-center h-[60vh] gap-3">
        <span className="text-5xl">📋</span>
        <p className="text-[#605E5C] text-lg font-medium">No report available.</p>
        <p className="text-sm text-gray-400">Run an analysis to see business strategy insights.</p>
      </div>
    );
  }

  const business = report?.business ?? {};
  const metadata = report.metadata || {};

  const customerSegments           = arr(business.customer_segments);
  const customerPainPoints         = arr(business.customer_pain_points);
  const customerPersonas           = arr(business.customer_personas);
  const acquisitionChannels        = arr(business.acquisition_channels);
  const revenueStreams              = arr(business.revenue_streams);
  const marketingChannels          = arr(business.marketing_channels);
  const distributionChannels       = arr(business.distribution_channels);
  const growthRoadmap              = arr(business.growth_roadmap);
  const keyAdvantages              = arr(business.key_advantages);
  const competitiveDifferentiators = arr(business.competitive_differentiators);

  const swot = report.swot ?? {};
  const strengths     = arr(swot.strengths);
  const weaknesses    = arr(swot.weaknesses);
  const opportunities = arr(swot.opportunities);
  const threats       = arr(swot.threats);

  const recommendations: string[] = arr(report.investor?.recommendations);

  const generatedAt = metadata.generated_at
    ? new Date(metadata.generated_at).toLocaleString("en-US", {
        dateStyle: "medium",
        timeStyle: "short",
      })
    : null;

  return (
    <div className="space-y-8 text-gray-700">

      {/* ── Header ── */}
      <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-[#323130]">Business Strategy</h1>
          <p className="text-sm text-[#605E5C] mt-1">
            AI-generated business intelligence ·{" "}
            <span className="text-[#0078D4] font-medium">Business Strategy Agent</span>
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
            ✓ AI-Generated Report
          </span>
        </div>
      </div>

      {/* ── Executive Summary Banner ── */}
      {report.executive_summary?.executive_summary && (
        <div className="bg-[#E5F1FB] border-l-4 border-[#0078D4] p-5 rounded-xl">
          <h3 className="font-semibold text-[#0078D4] text-base flex items-center gap-2 mb-1">
            <span>🤖</span> Business Strategy Summary
          </h3>
          <p className="text-[#323130] text-sm leading-6">
            {report.executive_summary.executive_summary}
          </p>
        </div>
      )}

      {/* ── KPI Cards ── */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-5">
        <MetricCard
          icon="🏗️"
          label="Business Model"
          value={business.business_model ? "Defined" : "N/A"}
          sub={business.business_model?.split(" ").slice(0, 5).join(" ") + "…"}
          accentColor="#0078D4"
        />
        <MetricCard
          icon="👥"
          label="Segments"
          value={String(customerSegments.length || "N/A")}
          sub="Customer segments"
          accentColor="#107C10"
        />
        <MetricCard
          icon="💰"
          label="Revenue Streams"
          value={String(revenueStreams.length || "N/A")}
          sub="Identified streams"
          accentColor="#8764B8"
        />
        <MetricCard
          icon="📣"
          label="Marketing Channels"
          value={String(marketingChannels.length || "N/A")}
          sub="Channels identified"
          accentColor="#F7630C"
        />
        <MetricCard
          icon="🏆"
          label="Advantages"
          value={String(keyAdvantages.length || "N/A")}
          sub="Competitive edges"
          accentColor="#00B7C3"
        />
        <MetricCard
          icon="💪"
          label="SWOT Strengths"
          value={String(strengths.length || "N/A")}
          sub="Identified by SWOT Agent"
          accentColor="#107C10"
        />
      </div>

      {/* ── Business Overview ── */}
      <SectionCard icon="🏢" title="Business Overview">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <InfoCard label="Business Model"    value={val(business.business_model)} />
          <InfoCard label="Startup Vision"    value={val(business.startup_vision)} />
          <InfoCard label="Mission Statement" value={val(business.mission_statement)} />
          <InfoCard label="Value Proposition" value={val(business.value_proposition)} accent="#107C10" />
          <div className="md:col-span-2">
            <InfoCard label="Unique Selling Proposition (USP)" value={val(business.usp)} accent="#8764B8" />
          </div>
        </div>
      </SectionCard>

      {/* ── Customer Analysis ── */}
      <SectionCard icon="👥" title="Customer Analysis" badge={customerSegments.length > 0 ? `${customerSegments.length} segments` : undefined}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          <div>
            <InfoCard label="Target Customer" value={val(business.target_customer)} />
          </div>

          <div className="space-y-4">
            <div>
              <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">Customer Segments</p>
              <TagList items={customerSegments} emptyText="No segments identified." icon="→" />
            </div>
          </div>

          <div>
            <p className="text-xs font-semibold text-[#D13438] uppercase tracking-wide mb-2">Customer Pain Points</p>
            <TagList items={customerPainPoints} emptyText="No pain points identified." icon="!" colorClass="text-[#D13438]" />
          </div>

          <div>
            <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-2">Acquisition Channels</p>
            <TagList items={acquisitionChannels} emptyText="No channels identified." icon="✓" colorClass="text-[#107C10]" />
          </div>

          {customerPersonas.length > 0 && (
            <div className="md:col-span-2">
              <p className="text-xs font-semibold text-[#8764B8] uppercase tracking-wide mb-2">Customer Personas</p>
              <div className="flex flex-wrap gap-2">
                {customerPersonas.map((p, i) => (
                  <span key={i} className="bg-[#F3F2F1] text-[#323130] text-xs px-3 py-1.5 rounded-full border border-gray-200">
                    👤 {p}
                  </span>
                ))}
              </div>
            </div>
          )}

        </div>
      </SectionCard>

      {/* ── Revenue Strategy ── */}
      <SectionCard icon="💰" title="Revenue Strategy" badge={revenueStreams.length > 0 ? `${revenueStreams.length} streams` : undefined}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
          <InfoCard label="Revenue Model"         value={val(business.revenue_model)} />
          <InfoCard label="Pricing Strategy"      value={val(business.pricing_strategy)} />
          <InfoCard label="Monetization Strategy" value={val(business.monetization_strategy)} accent="#107C10" />
          <InfoCard label="Expected Revenue Growth" value={val(business.expected_revenue_growth)} accent="#107C10" />
        </div>
        <div>
          <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">Revenue Streams</p>
          <TagList items={revenueStreams} emptyText="No revenue streams identified." icon="💵" />
        </div>
      </SectionCard>

      {/* ── Go-To-Market Strategy ── */}
      <SectionCard icon="🚀" title="Go-To-Market Strategy">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
          <div className="md:col-span-2">
            <InfoCard label="Go-To-Market Strategy" value={val(business.go_to_market)} />
          </div>
          <InfoCard label="Sales Strategy"       value={val(business.sales_strategy)} />
          <InfoCard label="Partnership Strategy" value={val(business.partnership_strategy)} accent="#8764B8" />
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">Marketing Channels</p>
            <TagList items={marketingChannels} emptyText="No marketing channels listed." icon="📣" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-2">Distribution Channels</p>
            <TagList items={distributionChannels} emptyText="No distribution channels listed." icon="📦" colorClass="text-[#107C10]" />
          </div>
        </div>
      </SectionCard>

      {/* ── Growth Strategy ── */}
      <SectionCard icon="📈" title="Growth Strategy">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          <InfoCard label="Expansion Strategy"     value={val(business.expansion_strategy)} />
          <InfoCard label="Scaling Plan"           value={val(business.scaling_plan)} />
          <InfoCard label="Market Expansion"       value={val(business.market_expansion)} accent="#107C10" />
          {business.international_expansion && (
            <InfoCard label="International Expansion" value={business.international_expansion} accent="#00B7C3" />
          )}
        </div>
        <div>
          <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-3">Growth Roadmap</p>
          <RoadmapTimeline steps={growthRoadmap} />
        </div>
      </SectionCard>

      {/* ── Competitive Advantage ── */}
      <SectionCard icon="🏆" title="Competitive Advantage" badge={keyAdvantages.length > 0 ? `${keyAdvantages.length} advantages` : undefined}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
          <InfoCard label="Innovation Strategy"  value={val(business.innovation_strategy)} />
          <InfoCard label="AI Advantage"         value={val(business.ai_advantage)} accent="#8764B8" />
          <div className="md:col-span-2">
            <InfoCard label="Technology Advantage" value={val(business.technology_advantage)} accent="#00B7C3" />
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <p className="text-xs font-semibold text-[#0078D4] uppercase tracking-wide mb-2">Key Advantages</p>
            <TagList items={keyAdvantages} emptyText="No advantages listed." icon="⭐" />
          </div>
          <div>
            <p className="text-xs font-semibold text-[#107C10] uppercase tracking-wide mb-2">Competitive Differentiators</p>
            <TagList items={competitiveDifferentiators} emptyText="No differentiators listed." icon="✓" colorClass="text-[#107C10]" />
          </div>
        </div>
      </SectionCard>

      {/* ── SWOT Snapshot ── */}
      <SectionCard icon="🔲" title="SWOT Snapshot">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <SwotQuadrant icon="💪" label="Strengths"     items={strengths}     borderColor="#107C10" bgColor="#F0FBF0" iconColor="#107C10" />
          <SwotQuadrant icon="⚠️" label="Weaknesses"    items={weaknesses}    borderColor="#D13438" bgColor="#FEF3F3" iconColor="#D13438" />
          <SwotQuadrant icon="🚀" label="Opportunities" items={opportunities} borderColor="#0078D4" bgColor="#EBF3FB" iconColor="#0078D4" />
          <SwotQuadrant icon="🛑" label="Threats"       items={threats}       borderColor="#FF8C00" bgColor="#FFF8EE" iconColor="#FF8C00" />
        </div>
      </SectionCard>

      {/* ── AI Recommendations ── */}
      <SectionCard icon="🤖" title="AI Recommendations">
        {recommendations.length > 0 ? (
          <ol className="space-y-2">
            {recommendations.map((r, i) => (
              <li key={i} className="flex items-start gap-2 text-sm text-[#323130] leading-6 bg-[#F3F2F1] rounded-lg px-4 py-2">
                <span className="shrink-0 font-bold text-[#0078D4]">{i + 1}.</span>
                <span>{r}</span>
              </li>
            ))}
          </ol>
        ) : (
          <p className="text-sm text-[#605E5C]">No AI recommendations available.</p>
        )}
      </SectionCard>

      {/* ── Footer Branding ── */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 pt-2 border-t border-gray-200">
        <p className="text-xs text-[#605E5C]">
          Powered by{" "}
          <span className="font-semibold text-[#0078D4]">Microsoft Azure AI Foundry</span>{" "}
          · Business Strategy Agent
        </p>
        {generatedAt && (
          <p className="text-xs text-[#605E5C]">Report generated: {generatedAt}</p>
        )}
      </div>

    </div>
  );
}

