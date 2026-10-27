# Real contribution snake

A manual, read-only workflow uses Platane/snk at a full commit SHA. Upstream was checked
on 2026-10-27: not archived, latest push 2026-10-18; v3 commit dated 2026-04-25.
It fetches `darcykun`'s real contribution graph and uploads generated SVGs as a run
artifact. No synthetic graph, automated contribution commits, or public output branch
is created. Authentication is currently absent, so generation has not been verified.

After the approved profile push, dispatch this workflow, inspect the actual artifact,
then approve adding those SVGs to `assets/` and embedding a light/dark picture element.
The README deliberately has no broken graph URL. Static-profile.md stays motion-free.
A refresh schedule is optional later and requires an approved policy for remote writes.

Upstream: https://github.com/Platane/snk
