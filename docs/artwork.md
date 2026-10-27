# Artwork, type and accessibility

## Banner selection

The requested `1037164989160119459.jpeg` was found in the supplied kit: RGB JPEG,
736 × 238 pixels, 27,366 bytes. It is a tight horizontal crop of a manga eye with
black hair, ink shadows and screentone. Its composition was inspected; it can display
at 736px without enlargement. No source artist, permission record or redistribution
license was supplied, so it is not included in this repository.

`assets/manga-eyes-original.webp` is the original replacement: a close crop across
two calm eyes, asymmetrical hair and shadows, and fine monochrome hatching. Created
from a written description, without the supplied image as input. It does not reproduce
a specific panel or character. The complete generated composition is retained; only
proportional resizing and WebP encoding were applied. Served from this repository,
with no image-generation endpoint at runtime.

Generation prompt: original monochrome manga-inspired editorial banner, ultra-wide
horizontal crop across both eyes and eyebrows of an invented adult character;
calm, thoughtful gaze; dark hair partially obscuring one edge; ink linework,
cross-hatching and screentone; black and white; no existing character or panel,
text, logo, watermark, glow, supernatural markings, or full-body composition.
Created with the built-in OpenAI imagegen tool. See assets/NOTICE.txt for rights scope.

## Custom title

`dar-kun-title.svg` (dark backgrounds) and `dar-kun-title-light.svg` (light backgrounds)
use the same original hand-constructed geometric paths. The lettering was drawn as
vector shapes rather than converted from a typeface. No font is bundled or used to
generate these paths, so no third-party font license is required. Source is MIT
licensed. Each SVG has a title and description; the README image also has the
accessible alternative “Dar KUN!”.

The dark variant uses soft white → ice blue → ocean blue. The light variant uses
midnight navy → deep ocean → ocean blue. Picture/source markup selects the dark
asset by color preference, with a legible light fallback.

## Mascot and retained assets

The existing original mascot design is unchanged, including its 72px GIF and static
PNG. It is displayed at 52px near the footer as a small accent. The picture element
selects the static PNG for reduced-motion preferences. A separate static profile
provides a dependable no-animation option if a client ignores that preference.

Original mascot prompt: brown tousled hair, black rectangular glasses, small red bow,
navy outfit and ice-blue accents; transparent background; aligned neutral, blink and
wave frames; no copied character, text, logos or watermarks. Built-in OpenAI imagegen.

The previous ocean banner and typing assets are retained, not deleted. They are not
used in the new hero: a static title and one small mascot create a calmer hierarchy.
No external CSS or scripts are needed by the published README.

## Japanese wording

`ダルくん` is a casual Japanese-script rendering of the supplied nickname, not a
professional title. `静かに、確実に。` pairs two natural adverbial forms: quietly/calmly
and surely/reliably. It is an intentional short motto, not a complete sentence;
“Quietly, but surely” is an idiomatic English rendering. Japanese appears in two
places only. Dictionary checks: [静か](https://kotobank.jp/word/静か-519671) and
[確実](https://kotobank.jp/word/確実-460275), Digital Daijisen entries via Kotobank.
