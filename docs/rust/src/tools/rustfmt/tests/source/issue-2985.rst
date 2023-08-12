src/tools/rustfmt/tests/source/issue-2985.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
fn foo() {
    {
        {
            let extra_encoder_settings = extra_encoder_settings.iter()
                                                               .filter_map(|&(name, value)| {
                                                         value.split()
                                                              .next()
                                                              .something()
                                                              .something2()
                                                              .something3()
                                                              .something4()
                                                     });
            let extra_encoder_settings = extra_encoder_settings.iter()
                                                               .filter_map(|&(name, value)| {
                                                                               value.split()
                                                                                    .next()
                                                                                    .something()
                                                                                    .something2()
                                                                                    .something3()
                                                                                    .something4()
                                                                           })
                                                               .something();
            if let Some(subpod) = pod.subpods.iter().find(|s| {
                                                              !s.plaintext
                                                                .as_ref()
                                                                .map(String::as_ref)
                                                                .unwrap_or("")
                                                                .is_empty()
                                                          }) {
                do_something();
            }
        }
    }
}


