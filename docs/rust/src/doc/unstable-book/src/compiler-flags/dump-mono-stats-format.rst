src/doc/unstable-book/src/compiler-flags/dump-mono-stats-format.md
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `dump-mono-stats-format`

--------------------

The `-Z dump-mono-stats-format` compiler flag controls what file format to use for `-Z dump-mono-stats`.
The default is markdown; currently JSON is also supported. JSON can be useful for programatically manipulating the results (e.g. to find the item that took the longest to compile).


