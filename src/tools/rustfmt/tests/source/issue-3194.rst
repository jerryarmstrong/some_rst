src/tools/rustfmt/tests/source/issue-3194.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m { struct S where A: B; }

mod n { struct Foo where A: B { foo: usize } }

mod o { enum Bar where A: B { Bar } }

mod with_comments {
  mod m { struct S /* before where */ where A: B; /* after where */ }
  
  mod n { struct Foo /* before where */ where A: B /* after where */ { foo: usize } }
  
  mod o { enum Bar /* before where */ where A: B /* after where */ { Bar } }
}


