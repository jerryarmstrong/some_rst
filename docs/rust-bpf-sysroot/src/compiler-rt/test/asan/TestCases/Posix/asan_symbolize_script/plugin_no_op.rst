src/compiler-rt/test/asan/TestCases/Posix/asan_symbolize_script/plugin_no_op.py
===============================================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    class NoOpPlugin(AsanSymbolizerPlugIn):
  def register_cmdline_args(self, parser):
    logging.info('Adding --unlikely-option-name-XXX option')
    parser.add_argument('--unlikely-option-name-XXX', type=int, default=0)

  def process_cmdline_args(self, pargs):
    logging.info('GOT --unlikely-option-name-XXX=%d', pargs.unlikely_option_name_XXX)
    return True

  def destroy(self):
    logging.info('destroy() called on NoOpPlugin')

  def filter_binary_path(self, path):
    logging.info('filter_binary_path called in NoOpPlugin')
    return path

register_plugin(NoOpPlugin())


