src/v2/components/TourDeSol/Cards/styles.js
===========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';

export default makeStyles({
  cards: {
    '& > *:not(:last-child)': {
      marginBottom: 20,
    },
    '& svg': {
      height: '138px',
      width: '100%',
      '&:not(:last-child)': {
        marginBottom: 14,
      },
    },
  },
});


