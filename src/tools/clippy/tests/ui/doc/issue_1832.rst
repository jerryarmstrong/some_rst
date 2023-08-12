src/tools/clippy/tests/ui/doc/issue_1832.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Ok: <http://www.unicode.org/reports/tr9/#Reordering_Resolved_Levels>
///
/// Not ok: http://www.unicode.org
/// Not ok: https://www.unicode.org
/// Not ok: http://www.unicode.org/
/// Not ok: http://www.unicode.org/reports/tr9/#Reordering_Resolved_Levels
fn issue_1832() {}

fn main() {}


