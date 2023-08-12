src/tools/rustfmt/tests/source/issue_4579.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-hard_tabs: true

#[macro_export]
macro_rules! main {
	() => {
		#[spirv(fragment)]
		pub fn main_fs(
			mut out_color: ::spirv_std::storage_class::Output<Vec4>,
			#[spirv(descriptor_set = 1)]iChannelResolution: ::spirv_std::storage_class::UniformConstant<
				[::spirv_std::glam::Vec3A; 4],
			>,
		) {
		}
	};
}


