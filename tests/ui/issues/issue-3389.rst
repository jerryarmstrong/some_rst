tests/ui/issues/issue-3389.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

struct trie_node {
    content: Vec<String> ,
    children: Vec<trie_node> ,
}

fn print_str_vector(vector: Vec<String> ) {
    for string in &vector {
        println!("{}", *string);
    }
}

pub fn main() {
    let mut node: trie_node = trie_node {
        content: Vec::new(),
        children: Vec::new()
    };
    let v = vec!["123".to_string(), "abc".to_string()];
    node.content = vec!["123".to_string(), "abc".to_string()];
    print_str_vector(v);
    print_str_vector(node.content.clone());

}


