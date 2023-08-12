src/tools/rustfmt/tests/source/markdown-comment.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Preserve two trailing whitespaces in doc comment,
// but trim any whitespaces in normal comment.

//! hello world  
//! hello world 

/// hello world    
/// hello world 
/// hello world  
fn foo() {
    // hello world  
    // hello world 
    let x = 3;
    println!("x = {}", x);
}


