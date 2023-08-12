src/tools/rustfmt/tests/source/issue-447.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true

fn main() {
	if /* shouldn't be dropped
	shouldn't be dropped */
	
	cond /* shouldn't be dropped
	shouldn't be dropped */
	
	{
	} /* shouldn't be dropped
	shouldn't be dropped */
	
	else /* shouldn't be dropped
	shouldn't be dropped */
	
	if /* shouldn't be dropped
	shouldn't be dropped */
	
	cond /* shouldn't be dropped
	shouldn't be dropped */
	
	{
	} /* shouldn't be dropped
	shouldn't be dropped */
	
	else /* shouldn't be dropped
	shouldn't be dropped */
	
	{
	}
	
	if /* shouldn't be dropped
	shouldn't be dropped */
	let Some(x) = y/* shouldn't be dropped
	shouldn't be dropped */
	{
	}
}


