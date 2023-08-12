src/tools/rustfmt/tests/source/issue-3840/version-one_hard-tabs.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-hard_tabs: true

impl<Target: FromEvent<A> + FromEvent<B>, A: Widget2<Ctx = C>, B: Widget2<Ctx = C>, C: for<'a> CtxFamily<'a>> Widget2 for WidgetEventLifter<Target, A, B>
{
    type Ctx = C;
    type Event = Vec<Target>;
}

mod foo {
    impl<Target: FromEvent<A> + FromEvent<B>, A: Widget2<Ctx = C>, B: Widget2<Ctx = C>, C: for<'a> CtxFamily<'a>> Widget2 for WidgetEventLifter<Target, A, B>
    {
        type Ctx = C;
        type Event = Vec<Target>;
    }
}


