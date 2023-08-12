src/v2/components/TourDeSol/Table/styles.js
===========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  root: {
    marginTop: 19,
    background: getColor('grey2')(theme),
    padding: '25px 44px',
    flex: 1,
    [theme.breakpoints.down('sm')]: {
      padding: 0,
      paddingBottom: 27,
      marginBottom: 50,
    },
  },
  header: {
    display: 'flex',
    alignItems: 'baseline',
    flexWrap: 'wrap',
    '& *:first-child': {
      marginRight: 35,
    },
    marginBottom: 23,
    [theme.breakpoints.down('sm')]: {
      padding: '10px 27px 0',
      marginBottom: 10,
    },
  },
  link: {
    marginLeft: 'auto',
    textTransform: 'uppercase',
    color: getColor('main')(theme),
    fontSize: 15,
    textDecoration: 'none',
  },
  list: {
    display: 'flex',
    width: '100%',
    overflowX: 'auto',
  },
  vertical: {
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'column',
    },
  },
  card: {
    padding: 17,
    background: '#505050',
    marginRight: 12,
    maxWidth: 326,
  },
  cardVertical: {
    [theme.breakpoints.down('sm')]: {
      marginBottom: 2,
      marginRight: 0,
      maxWidth: '100%',
    },
  },
  cardTitle: {
    fontSize: 12,
    textTransform: 'uppercase',
    color: '#C4C4C4',
    letterSpacing: 2,
    fontWeight: 'bold',
  },
}));


