# Contributing to the PSForever website and wiki

The site is built with [Zensical](https://zensical.org/) and configured in
`zensical.toml`. Wiki pages are Markdown files under `wiki/`, and pushes
to `main` publish the site.

## Preview locally with Docker

You need [Docker](https://docs.docker.com/get-started/get-docker/) (Docker
Desktop on Windows and macOS). From the repository root:

```sh
docker compose watch
```

Open <http://localhost:8000/> for the landing page and
<http://localhost:8000/wiki/> for the wiki's front page. The first start builds an image
that includes the site, which takes a minute. After that, saving a file
refreshes the browser within a few seconds. Stop the preview with `Ctrl+C`,
then `docker compose down`.

The preview runs on a copy of the site inside the container, and
`docker compose watch` copies each change you save into it. (Zensical can't
see changes made through a plain Docker bind mount on Windows or macOS, so
`docker compose up` on its own shows the site but doesn't refresh.) Changes to
`zensical.toml` restart the preview, and changes to `requirements.txt` or
`src/` rebuild the image.

## Check before opening a pull request

```sh
docker compose run --rm check
```

This runs the same steps as CI: a strict build that fails on any warning, such
as a link to a page or section that does not exist, followed by the redirect
script. It works on a copy, so it writes nothing to your checkout.

## Editing in a dev container

The repository includes a [dev container](https://containers.dev/) built from
the same `Dockerfile`. In VS Code, run **Dev Containers: Reopen in Container**,
then start the preview from the container's terminal:

```sh
zensical serve --dev-addr=0.0.0.0:8000
```

Port 8000 is forwarded automatically.

## Wiki pages

- Put pages in the category folder they belong to under `wiki/`, and images
  in `wiki/images/`. A page's address follows its path: `wiki/weapons/Spiker.md`
  is served at `/weapons/Spiker/`. Link between pages with relative paths, such
  as `../weapons/Spiker.md`.
- Link to a section with its generated ID: lowercase, with spaces turned into
  hyphens, for example `Adaptive_Construction_Engine.md#spitfire-turret`.
- Use file names that work on every operating system: no `"`, `:`, `*`, `?`,
  `<`, `>`, or `|`, and never two names that differ only by letter case.
- Other sites link to wiki pages and images, so avoid renaming or moving them.
  If you must, add the old URL to `RENAMED` in `scripts/redirects.py`, which
  runs after every build in CI and forwards the old URL to the new one. Images
  can't be redirected.
- The sidebar lists pages alphabetically by file name, except in sections
  listed in `version_sorted_sections` in `zensical.toml` (currently Patches),
  which sort as version numbers: `3.2.12` before `3.15.6`. Name patch pages by
  their version (`3.15.6.md`); an addendum can add a suffix
  (`3.7.10_Addendum.md`) and sorts right after its version.

## Landing page and header

The landing page is `overrides/home.html`, styled by
`wiki/assets/stylesheets/psforever.css`. Its background images rotate every
8 seconds and are listed under `[[project.extra.hero_images]]` in
`zensical.toml`. To preview one image on its own, add `?hero=N` to the URL, for
example <http://localhost:8000/?hero=2>. Each image can also set:

- `position`: a CSS `background-position` for tablets and desktops, such as
  `"center 70%"` to show more of the lower part of the picture.
- `focus`: the horizontal point to keep centered on phones, where only a narrow
  slice of the picture fits, such as `"25%"` for a subject on the left.
- `flip = true`: mirror the picture on tablets and desktops, so a subject on
  its left shows beside the text instead of under it. Don't use it on pictures
  with readable text in them.
- `align = "right"`: place the art on the right half, fading out behind the
  text. Use it for artwork with a subject in the middle, like the splash image.
- `mobile_align = "corner"`: on phones only, shrink the art so its center sits
  in the hero's upper-right corner, above the headline. The splash image uses
  it to keep its logo clear of the text.
- `vivid = true`: keep the image's colors instead of dimming it. Use it for
  PSForever's own artwork; game screenshots are dimmed so the text stays
  readable.

Check a new image at phone and desktop widths with `?hero=N` before adding it.

The Home, Wiki, and Portal links come from `[[project.extra.header_links]]` in
`zensical.toml`. Give site links a path from the site root (`/wiki/`); a full
URL (`https://play.psforever.net/`) becomes an external link with an icon.
A site link is highlighted on pages under its path. Wiki pages live at the site
root, so the Wiki link sets `everywhere_else = true`, which highlights it on
every page except the landing page. The wiki front page (`wiki/wiki.md`) is
listed right after Home in the sidebar. On
tablets and desktops they appear in the header (`overrides/partials/header.html`);
on phones they move to the top of the menu drawer
(`overrides/partials/psf-drawer-links.html`, included from
`overrides/partials/nav.html`). `header.html`, `nav.html`, and `nav-item.html`
(which does the version sorting) are copies of Zensical's own templates with
these additions, so compare them with the new versions when upgrading
Zensical.

PSForever is a fan project and isn't affiliated with the owners of PlanetSide.
Keep the landing page that way:

- Use screenshots captured on PSForever for new hero images. Don't use
  official logos, faction emblems, box art, or marketing renders.
- Refer to the game by name to say what PSForever is compatible with, but don't
  style "PlanetSide" as a logo or suggest the project is official or endorsed.
- Don't link to copies of the game client from the landing page.
- Keep the disclaimer in `copyright` in `zensical.toml`; it appears in the
  footer of every page.
