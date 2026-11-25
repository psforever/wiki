# PSForever website and wiki

This repository is the source for [www.psforever.net](https://www.psforever.net/),
the public website of [PSForever](https://github.com/psforever): a free,
open-source server emulator that lets people play the original PlanetSide again.

The site has two parts:

- **A landing page** at `/` for people discovering the project. It explains what
  PSForever is, shows how to get into the game, introduces the three empires,
  and points to the Discord community and its weekly Sunday sessions.
- **The PSForever wiki**, a community reference of about 1,000 pages on
  weapons, vehicles, certifications, facilities, game history, and more. Its
  front page is at `/wiki/`, and each page keeps its long-standing address
  (for example `/weapons/Spiker/`). Much of it was carried over from earlier
  PlanetSide fan wikis.

The header also links to the [PSForever Portal](https://play.psforever.net/),
where players check server status, manage their account, and look up character
stats. The portal is a separate project
([PSFPortal](https://github.com/psforever/PSFPortal)).

## Quick start

You only need [Docker](https://docs.docker.com/get-started/get-docker/)
(Docker Desktop on Windows and macOS). From the repository root, run:

```sh
docker compose watch
```

Then open <http://localhost:8000/>. The first start takes about a minute.
After that, every file you save shows up in the browser within a few seconds.
Press `Ctrl+C` to stop, then run `docker compose down`.

Before you open a pull request, run the same check that CI runs:

```sh
docker compose run --rm check
```

It builds the whole site in strict mode and fails on any broken link.

## Making common changes

| I want to… | Do this |
| --- | --- |
| Fix or expand a wiki page | Edit its Markdown file under `wiki/`. Every wiki page also has an edit button that opens the file on GitHub. |
| Add a wiki page | Create a `.md` file in the category folder it belongs to (for example `wiki/weapons/`), starting with a `# Title` line. It appears in the sidebar automatically. |
| Add an image to a page | Put the image in `wiki/images/` and add `![Caption](../images/name.jpg){ class="figure" }` below the page title. Pages in deeper folders need one more `../` per level. |
| Change the landing page | Edit `overrides/home.html`. Its styles are in `wiki/assets/stylesheets/psforever.css`. |
| Change the landing page's background images | Edit the `[[project.extra.hero_images]]` list in `zensical.toml`. Preview one with `?hero=2` on the URL. |
| Change the header links | Edit `[[project.extra.header_links]]` in `zensical.toml`. |

[CONTRIBUTING.md](CONTRIBUTING.md) covers each of these in more detail,
including file-naming rules and what the landing page may and may not show.

## What's in the wiki

The wiki is organized into categories, each a folder under `wiki/`:

| Category | Pages | What it covers |
| --- | --- | --- |
| Weapons, Ammunition | 72, 49 | Infantry weapons and what they fire |
| Vehicles | 43 | Ground vehicles, aircraft, and transports |
| Armor, Implants, Modules | 15, 11, 7 | Exo-suits, MAX units, implants, and modules |
| Items | 64 | Deployables, tools, and terminals |
| Certifications, Merits | 51, 88 | How characters unlock equipment, and the awards they earn |
| Facilities, Locations | 115, 76 | Bases, towers, continents, and other places |
| Factions | 4 | The three empires and the Black Ops |
| Terminology, Chat | 140, 9 | Game concepts, slang, and in-game chat |
| Training | 12 | The game's training missions, step by step |
| Patches | 125 | The game's patch history |
| Archive | 136 | Historical outfits, events, servers, and player guides |
| PSForever | 1 | The connection guide for getting into the game |

## How the site is built

The site is a static website built with [Zensical](https://zensical.org/), the
successor to Material for MkDocs. It turns the Markdown files in `wiki/` into
HTML, using a theme customized for PSForever.

- **Configuration** lives in `zensical.toml`: the site's name and address, the
  theme and its features, the landing page's background images, and the header
  links.
- **Theme changes** live in `overrides/`. `home.html` is the landing page.
  `partials/header.html` adds the Home, Wiki, and Portal links to the header;
  it's a copy of Zensical's own header, so compare it with the new version when
  upgrading Zensical.
- **Look and behavior** come from `wiki/assets/` and `wiki/res/`: the logo,
  the self-hosted fonts (with their licenses), the stylesheet that gives the site its dark
  theme, and a small script that rotates the landing page's images and shows
  the weekly session in each visitor's time zone.
- **Figures**: `src/figure/` is a small Markdown extension that turns images
  marked `{ class="figure" }` into captioned figures that float beside the text
  and enlarge when clicked.
- **Redirects**: after each build, `scripts/redirects.py` writes a small page
  at the old address of each renamed or moved wiki page that forwards to its
  new address, so old links keep working.

### Publishing

Every pull request is built in strict mode by GitHub Actions
(`.github/workflows/publish.yaml`), so broken links are caught before they're
merged. When a change lands on `main`, the same workflow builds the site, writes
the redirects, and publishes the result to the `gh-pages` branch. GitHub Pages
serves that branch at www.psforever.net, set by the `CNAME` file in `wiki/`.

### Repository layout

| Path | What it holds |
| --- | --- |
| `zensical.toml` | Site configuration |
| `wiki/` | Wiki pages, organized by category folders |
| `wiki/index.md` | Landing page entry (its content is in `overrides/home.html`) |
| `wiki/wiki.md` | Wiki front page, served at `/wiki/` |
| `wiki/images/` | Images used by wiki pages |
| `wiki/res/` | Logo, favicon, and figure styles |
| `wiki/assets/` | Fonts, stylesheets, scripts, and site images |
| `overrides/` | Landing page and header templates |
| `scripts/redirects.py` | Writes redirects for renamed and moved pages |
| `src/figure/` | Markdown extension for captioned figures |
| `Dockerfile`, `compose.yaml` | Local preview and checks |
| `.devcontainer/` | Dev container for VS Code, using the same Dockerfile |
| `.github/workflows/` | Build and publish workflow |

## Known gaps

These are known and not yet fixed. Help is welcome on any of them.

- **Pages with little or no text.** Many facility pages have only a title and
  an image.
- **Images that show as text.** A handful of pages (such as the Merits index)
  put image links inside HTML blocks, where they appear as literal text instead
  of pictures.
- **A few malformed links**, left over from the old wiki, that the strict build
  doesn't detect.
- **No license.** The repository doesn't yet say under which terms its code and
  content may be reused. Much of the content came from older fan wikis.

## Community and related projects

- **Discord:** [discord.com/invite/SQf8cW8](https://discord.com/invite/SQf8cW8),
  where players organize, get help, and hear about events. The community meets
  every Sunday at 12:00 PM Eastern.
- **Server:** [PSF-LoginServer](https://github.com/psforever/PSF-LoginServer),
  the emulated PlanetSide server itself.
- **Launcher:** [GameLauncher](https://github.com/psforever/GameLauncher), which
  connects the game client to PSForever.
- **Portal:** [play.psforever.net](https://play.psforever.net/)
  ([source](https://github.com/psforever/PSFPortal)).

## Disclaimer

PSForever is a non-commercial fan project. It isn't affiliated with or endorsed
by Daybreak Game Company. PlanetSide and related names are trademarks of their
respective owners.
