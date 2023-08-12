src/v2/components/Accounts/Detail/styles.js
===========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';

export default makeStyles(theme => ({
  programTitle: {
    display: 'flex',
    alignItems: 'center',
    marginLeft: 100,
    marginRight: 'auto',
    overflow: 'hidden',
    '& div': {
      marginLeft: 15,
      display: 'flex',
      alignItems: 'center',
    },
    '& span': {
      overflow: 'hidden',
      textOverflow: 'ellipsis',
    },
    [theme.breakpoints.down('md')]: {
      flexWrap: 'wrap',
      marginLeft: 0,
    },
  },
  types: {
    '& > div:not(:last-child)': {
      marginRight: 8,
    },
  },
  spec: {
    display: 'flex',
    flexWrap: 'wrap',
    padding: 0,
    [theme.breakpoints.down('xs')]: {
      flexDirection: 'column',
    },
  },
  tabs: {
    marginBottom: 50,
  },
  indicator: {
    display: 'none',
  },
  loader: {
    marginTop: 40,
  },
}));


