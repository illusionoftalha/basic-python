# Contributing

Keep examples small, runnable and focused on one topic. Use Python 3.10+ and the
standard library for the main course; discuss optional integrations separately.

1. Create a topic branch.
2. Add or improve a lesson with a short explanation and a main guard.
3. Add the command and a practice task to the learning path.
4. Test behavior with meaningful boundary cases, especially project validation.
5. Run `python scripts/check.py` from the repository root.
6. Open a focused PR describing the learner problem, change and check results.

Examples must not require credentials, contact external services or overwrite
personal files. Use temporary directories for file demonstrations and tests.
Preserve the existing ownership and license notice; this repository does not
grant an open-source license merely because it is public.
