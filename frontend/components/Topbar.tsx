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

        {/* Microsoft Logo */}

        <div className="grid grid-cols-2 gap-[2px]">

          <div className="w-4 h-4 bg-[#f25022]" />
          <div className="w-4 h-4 bg-[#7fba00]" />
          <div className="w-4 h-4 bg-[#00a4ef]" />
          <div className="w-4 h-4 bg-[#ffb900]" />

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