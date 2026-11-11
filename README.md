# Commera Builder Plugin

A [Frappe Builder](https://github.com/frappe/builder) editor plugin for [Commera](https://github.com/bwhtech/commera) store themes.

On a page of a Commera theme, the editor toolbar shows a "Theme · Page" button. Its panel lets you:

- Switch between the theme's Home, Product Listing and Product Detail pages, and see if each one is Published, Edited or Draft.
- Pick the product or collection that the canvas previews.
- Publish the theme, make it the live storefront theme, and open the page on the store.

The plugin shows nothing on other pages, and nothing on a site without Commera.

## Requirements

- Commera, with Builder themes. Create a theme in the Commera dashboard at **Storefront > Themes > New theme**.
- Frappe Builder with plugin protocol 1.

## Install

In the Builder editor, open **Plugins**, find **Commera** in the Builder Hub catalog, and install it.

## Files

- `manifest.json`: the plugin name, version and entry. Builder Hub reads it from the default branch.
- `main.js`: the plugin, one ES module. Builder supplies `builder`, `frappe-ui` and `vue`.
- `icon.svg`: the plugin icon.

The panel calls `commera.api.admin.builder_theme` on the site. That API is part of Commera.

## Release

1. Change `version` in `manifest.json`, and commit.
2. Build the package: `python3 scripts/package.py`.
3. Publish a GitHub release whose tag is the version, and attach the package:

   ```sh
   gh release create v<version> dist/bwhtech-commera-builder-plugin-<version>.builderplugin --title v<version>
   ```

Builder Hub checks the repository for new releases. A published release and its asset are immutable; to change one, release a new version.
