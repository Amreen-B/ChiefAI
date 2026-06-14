export default function Topbar() {

  return (

    <header
      className="
        h-[74px]
        bg-[#005a9e]
        flex
        items-center
        justify-between
        px-5
        border-b
        border-[#0a6ab5]
      "
    >

      {/* Left Side */}

      <div className="flex items-center">

        {/* ChiefAI Logo — abstract multi-agent network mark */}

        <div className="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center shrink-0">
          <svg
            width="26"
            height="26"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <defs>
              <linearGradient id="chiefaiGrad" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stopColor="#50E6FF" />
                <stop offset="55%" stopColor="#0078D4" />
                <stop offset="100%" stopColor="#8764B8" />
              </linearGradient>
            </defs>

            {/* Connection lines between agent nodes */}
            <path
              d="M16 8 L8 22 M16 8 L24 22 M8 22 L24 22"
              stroke="url(#chiefaiGrad)"
              strokeWidth="2"
              strokeLinecap="round"
              opacity="0.55"
            />

            {/* Top node (orchestrator) */}
            <circle cx="16" cy="8" r="4.5" fill="url(#chiefaiGrad)" />

            {/* Bottom-left agent node */}
            <circle cx="8" cy="22" r="3.5" fill="#FFFFFF" opacity="0.95" />

            {/* Bottom-right agent node */}
            <circle cx="24" cy="22" r="3.5" fill="#FFFFFF" opacity="0.95" />
          </svg>
        </div>

        {/* Divider */}

        <div className="mx-4 h-8 w-px bg-white/25" />

        {/* Title */}

        <div className="flex items-center gap-6">

          <h1
            className="
              text-white
              text-[18px]
              font-semibold
            "
          >
            ChiefAI
          </h1>

          <p
            className="
              text-blue-100
              text-[14px]
              font-normal
            "
          >
            Startup Intelligence Platform
          </p>

        </div>

      </div>

      {/* Right Side */}

      <div className="flex items-center gap-6">

        <input
          placeholder="Search startups, metrics..."
          className="
            w-[300px]
            h-[42px]
            bg-white/10
            border
            border-white/20
            rounded
            px-4
            text-white
            placeholder:text-blue-100
            outline-none
          "
        />

        <button className="text-white text-lg">
          🔔
        </button>

        <button className="text-white text-lg">
          ⚙️
        </button>

        <div
          className="
            w-10
            h-10
            rounded-full
            bg-[#ffcc00]
            text-black
            text-sm
            font-medium
            flex
            items-center
            justify-center
          "
        >
          ME
        </div>

      </div>

    </header>

  );

}