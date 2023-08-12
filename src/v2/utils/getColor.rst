src/v2/utils/getColor.js
========================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {get} from 'lodash/fp';
export default color => get(`palette.primary.${color}`);


