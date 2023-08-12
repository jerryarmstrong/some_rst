src/tools/rustfmt/tests/target/string-lit-2.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() -> &'static str {
    let too_many_lines = "Hello";
    let leave_me = "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss\
                    s
                    jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj";
}

fn issue_1237() {
    let msg = "eedadn\n\
               drvtee\n\
               eandsr\n\
               raavrd\n\
               atevrs\n\
               tsrnev\n\
               sdttsa\n\
               rasrtv\n\
               nssdts\n\
               ntnada\n\
               svetve\n\
               tesnvt\n\
               vntsnd\n\
               vrdear\n\
               dvrsen\n\
               enarar";
}


