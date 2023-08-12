src/tools/rustfmt/tests/source/visual-fn-type.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual
type CNodeSetAtts = unsafe extern "C" fn(node: *const RsvgNode,
                                         node_impl: *const RsvgCNodeImpl,
                                         handle: *const RsvgHandle,
                                         pbag: *const PropertyBag)
                                         ;
type CNodeDraw = unsafe extern "C" fn(node: *const RsvgNode,
                                      node_impl: *const RsvgCNodeImpl,
                                      draw_ctx: *const RsvgDrawingCtx,
                                      dominate: i32);


