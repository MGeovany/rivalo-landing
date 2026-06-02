from datetime import date

from fasthtml.common import *


CSS = """
:root {
  color-scheme: dark;
  --bg: #070806;
  --surface: rgba(255,255,255,.07);
  --surface-strong: rgba(255,255,255,.12);
  --line: rgba(255,255,255,.13);
  --text: #f7f8ed;
  --muted: rgba(247,248,237,.66);
  --dim: rgba(247,248,237,.44);
  --accent: #d7ff35;
  --accent-2: #ff8a3d;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  min-height: 100vh;
  background:
    radial-gradient(circle at 18% 12%, rgba(215,255,53,.22), transparent 28rem),
    radial-gradient(circle at 82% 8%, rgba(255,138,61,.18), transparent 24rem),
    linear-gradient(180deg, #090b07 0%, var(--bg) 52%, #020302 100%);
  color: var(--text);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  letter-spacing: -.02em;
}
a { color: inherit; text-decoration: none; }
.shell { width: min(1120px, calc(100% - 32px)); margin: 0 auto; }
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 22px 0;
}
.brand { display: flex; align-items: center; gap: 10px; font-weight: 800; letter-spacing: -.04em; }
.mark {
  width: 34px; height: 34px; border-radius: 12px;
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  box-shadow: 0 0 34px rgba(215,255,53,.22);
}
.links { display: flex; align-items: center; gap: 18px; color: var(--muted); font-size: 14px; }
.pill {
  display: inline-flex; align-items: center; gap: 8px;
  border: 1px solid var(--line); border-radius: 999px;
  padding: 8px 12px; background: rgba(255,255,255,.05);
  color: var(--muted); font-size: 13px;
}
.hero { padding: 84px 0 58px; display: grid; grid-template-columns: 1.05fr .95fr; gap: 56px; align-items: center; }
h1 { margin: 18px 0 18px; font-size: clamp(48px, 8vw, 92px); line-height: .89; letter-spacing: -.08em; }
.lead { color: var(--muted); font-size: clamp(18px, 2.2vw, 22px); line-height: 1.45; max-width: 640px; }
.cta { margin-top: 28px; display: flex; gap: 12px; flex-wrap: wrap; }
.button {
  display: inline-flex; align-items: center; justify-content: center;
  min-height: 48px; padding: 0 18px; border-radius: 999px;
  font-weight: 750; border: 1px solid transparent;
}
.button.primary { background: var(--accent); color: #111; }
.button.secondary { border-color: var(--line); background: rgba(255,255,255,.05); color: var(--text); }
.phone {
  position: relative; min-height: 560px; border: 1px solid var(--line); border-radius: 42px;
  background: linear-gradient(180deg, rgba(255,255,255,.14), rgba(255,255,255,.04));
  padding: 18px; box-shadow: 0 36px 120px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.18);
}
.screen { height: 100%; border-radius: 30px; background: #0c0f09; padding: 22px; overflow: hidden; }
.metric-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 22px; }
.card { border: 1px solid var(--line); background: var(--surface); border-radius: 24px; padding: 18px; }
.stat { font-size: 34px; font-weight: 850; letter-spacing: -.06em; }
.label { color: var(--dim); font-size: 12px; text-transform: uppercase; letter-spacing: .12em; }
.live { margin-top: 18px; height: 180px; border-radius: 22px; background: linear-gradient(135deg, rgba(215,255,53,.22), rgba(255,138,61,.12)); border: 1px solid rgba(215,255,53,.25); position: relative; overflow: hidden; }
.live:after { content: ""; position: absolute; inset: 34px 18px; border: 2px solid rgba(255,255,255,.26); border-radius: 18px; }
.dot { width: 8px; height: 8px; border-radius: 99px; background: var(--accent); box-shadow: 0 0 20px var(--accent); }
.section { padding: 52px 0; }
.section h2 { font-size: clamp(32px, 4vw, 54px); line-height: .95; margin: 0 0 14px; letter-spacing: -.06em; }
.section p { color: var(--muted); line-height: 1.65; }
.features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 28px; }
.feature h3 { margin: 12px 0 8px; font-size: 20px; }
.feature p { margin: 0; font-size: 15px; }
.legal { max-width: 820px; padding: 64px 0 90px; }
.legal h1 { font-size: clamp(42px, 7vw, 74px); }
.legal h2 { margin-top: 34px; }
.legal p, .legal li { color: var(--muted); line-height: 1.7; }
footer { border-top: 1px solid var(--line); padding: 28px 0 42px; color: var(--dim); font-size: 14px; }
@media (max-width: 820px) {
  .links { gap: 10px; font-size: 13px; }
  .hero { grid-template-columns: 1fr; padding-top: 40px; }
  .phone { min-height: 470px; }
  .features { grid-template-columns: 1fr; }
}
"""


app, rt = fast_app(
    hdrs=(
        Meta(charset="utf-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1"),
        Meta(name="theme-color", content="#070806"),
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;750;800;850&display=swap",
        ),
        Style(CSS),
    )
)


def shell(*children, title="Rivalo - Football performance tracking"):
    return Html(
        Head(Title(title)),
        Body(nav(), Main(*children), footer()),
    )


def nav():
    return Header(
        Div(
            A(Div(cls="mark"), Span("Rivalo"), href="/", cls="brand"),
            Nav(
                A("Support", href="/support"),
                A("Privacy", href="/privacy"),
                A("Terms", href="/terms"),
                cls="links",
            ),
            cls="shell nav",
        )
    )


def footer():
    year = date.today().year
    return Footer(
        Div(
            Span(f"Copyright {year} Rivalo. Built for amateur footballers."),
            cls="shell",
        )
    )


@rt("/")
def get():
    return shell(
        Section(
            Div(
                Div(
                    Span(Div(cls="dot"), "Live match tracking for football", cls="pill"),
                    H1("Your match, measured like a pro."),
                    P(
                        "Rivalo captures distance, sprints, heart rate, match context, rivalries, courts, goals, and personal records from iPhone and Apple Watch.",
                        cls="lead",
                    ),
                    Div(
                        A("Apple Support URL", href="/support", cls="button primary"),
                        A("Read Privacy Policy", href="/privacy", cls="button secondary"),
                        cls="cta",
                    ),
                ),
                phone_mock(),
                cls="shell hero",
            )
        ),
        Section(
            Div(
                H2("A simple performance layer for every match."),
                P("No complex setup. Start from Apple Watch, finish the match, and get a clean summary you can actually understand."),
                Div(
                    feature("01", "Live metrics", "Track distance, heart rate, sprints, intensity, and match duration."),
                    feature("02", "Context that matters", "Attach opponent, score, competition, surface, position, and court."),
                    feature("03", "Progress over time", "See records, streaks, goals, rivalries, and short post-match insights."),
                    cls="features",
                ),
                cls="shell section",
            )
        ),
    )


def phone_mock():
    return Div(
        Div(
            Span(Div(cls="dot"), "Live - 42:16", cls="pill"),
            Div(
                Div(Div("6.8", cls="stat"), Div("km", cls="label"), cls="card"),
                Div(Div("22", cls="stat"), Div("sprints", cls="label"), cls="card"),
                Div(Div("156", cls="stat"), Div("avg bpm", cls="label"), cls="card"),
                Div(Div("84", cls="stat"), Div("rating", cls="label"), cls="card"),
                cls="metric-grid",
            ),
            Div(cls="live"),
            cls="screen",
        ),
        cls="phone",
    )


def feature(icon, title, text):
    return Div(Div(icon, cls="stat"), H3(title), P(text), cls="card feature")


@rt("/support")
def get():
    return shell(
        article_page(
            "Support",
            P("Need help with Rivalo? This page is the official support URL for the app."),
            H2("Common help topics"),
            Ul(
                Li("Pair your Apple Watch and open Rivalo on both devices before starting a match."),
                Li("Allow Health permissions to record heart rate, distance, and workout activity."),
                Li("If a match does not sync immediately, reopen the iPhone app while the Watch is nearby."),
                Li("For account or data requests, contact support through the email listed below."),
            ),
            H2("Contact"),
            P("Email: support@rivalo.app"),
        ),
        title="Rivalo Support",
    )


@rt("/privacy")
def get():
    return shell(
        article_page(
            "Privacy Policy",
            P("Last updated: June 2, 2026."),
            P("Rivalo is designed to track football performance while keeping your data focused and limited to the app experience."),
            H2("Data we collect"),
            Ul(
                Li("Account information used for sign-in and profile setup."),
                Li("Workout metrics such as duration, distance, heart rate, sprints, calories, and route samples when you record a match."),
                Li("Match context you choose to add, such as score, opponent, competition, position, surface, and court."),
                Li("Local photos or venue notes you add inside the app."),
            ),
            H2("How we use data"),
            P("We use your data to provide match summaries, personal records, goals, streaks, rivalries, court stats, and performance insights."),
            H2("Sharing"),
            P("We do not sell personal data. Data is only shared with service providers required to run the app, such as authentication, database, hosting, and Apple platform services."),
            H2("Health data"),
            P("Apple Health data is used only to record and display your football activity. It is not used for advertising or sold to third parties."),
            H2("Contact"),
            P("For privacy requests, contact support@rivalo.app."),
        ),
        title="Rivalo Privacy Policy",
    )


@rt("/terms")
def get():
    return shell(
        article_page(
            "Terms of Use",
            P("Last updated: June 2, 2026."),
            H2("Use of Rivalo"),
            P("Rivalo provides football activity tracking and performance summaries. The app is not medical advice and should not be used as a substitute for professional guidance."),
            H2("Your responsibility"),
            P("Use Rivalo safely, follow local rules where you play, and stop activity if you feel pain, dizziness, or unsafe conditions."),
            H2("Availability"),
            P("We aim to keep Rivalo reliable, but the service may change or become unavailable during maintenance or updates."),
            H2("Contact"),
            P("Questions about these terms can be sent to support@rivalo.app."),
        ),
        title="Rivalo Terms of Use",
    )


def article_page(title, *content):
    return Div(Article(H1(title), *content, cls="legal"), cls="shell")
