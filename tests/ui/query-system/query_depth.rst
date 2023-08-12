tests/ui/query-system/query_depth.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

#![recursion_limit = "64"]
type Byte = Option<Option<Option<Option< Option<Option<Option<Option<
    Option<Option<Option<Option< Option<Option<Option<Option<
        Option<Option<Option<Option< Option<Option<Option<Option<
            Option<Option<Option<Option< Option<Option<Option<Option<
                Option<Option<Option<Option< Option<Option<Option<Option<
                    Option<Option<Option<Option< Option<Option<Option<Option<
                        Option<Option<Option<Option< Option<Option<Option<Option<
                            Option<Option<Option<Option< Option<Option<Option<Option<
                                Option<Option<Option<Option< Option<Option<Option<Option<
                                    Option<Option<Option<Option< Option<Option<Option<Option<
                                        Option<Option<Option<Option< Option<Option<Option<Option<
                                            Box<String>
                                        >>>> >>>>
                                    >>>> >>>>
                                >>>> >>>>
                            >>>> >>>>
                        >>>> >>>>
                    >>>> >>>>
                >>>> >>>>
            >>>> >>>>
        >>>> >>>>
    >>>> >>>>
>>>> >>>>;

fn main() {
//~^ ERROR: queries overflow the depth limit!
    println!("{}", std::mem::size_of::<Byte>());
}


