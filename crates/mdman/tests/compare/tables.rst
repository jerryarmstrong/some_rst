crates/mdman/tests/compare/tables.md
====================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: md

    # tables(1)

## DESCRIPTION

Testing tables.

| Single col |
--------------
| Hi! :) |


Header content | With `format` *text* | Another column
---------------|----------------------|----------------
Some data      | More data            |
Extra long amount of text within a column | hi | there


Left aligned | Center aligned | Right aligned
-------------|:--------------:|--------------:
abc | def | ghi


Left aligned | Center aligned | Right aligned
-------------|:--------------:|--------------:
X | X | X
Extra long text 123456789012 with mixed widths. | Extra long text 123456789012 with mixed widths. | Extra long text 123456789012 with mixed widths.


| Link check |
--------------
| [foo] |
| <https://example.com/> |


[foo]: https://example.com/


