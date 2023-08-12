src/v2/stores/transactions/timeline.js
======================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {action, flow, observable, decorate} from 'mobx';
import {apiGetTransactionsTimelinePage} from 'v2/api/transactions';
import _ from 'lodash';

class Store {
  isLoading = false;
  start = null;
  count = null;
  direction = null;
  res = {};
  transactions = [];
  transactionTimeline = {};
  transactionCount = null;
  next = null;
  prev = null;

  init = flow(function*({start, count, direction}) {
    if (
      this.transactionTimeline.pageInfo &&
      start === this.start &&
      count === this.count &&
      direction === this.direction
    ) {
      return this.transactionTimeline;
    }

    this.setLoading(true);
    this.start = start;
    this.count = count;
    this.direction = direction;

    const res = yield apiGetTransactionsTimelinePage({start, count, direction});

    this.res = res;

    this.transactionTimeline = res.data;
    this.transactions = _.map(res.data.pageData.results, x => x[1]);
    this.transactionCount = res.data.pageInfo.count;
    this.next = res.data.pageData.next;
    this.prev = res.data.pageData.prev;
    this.setLoading(false);

    return res;
  });
  setLoading(loading) {
    this.isLoading = loading;
  }
}

decorate(Store, {
  init: action.bound,
  start: observable,
  transactionTimeline: observable,
  transactions: observable,
  transactionCount: observable,
  next: observable,
  prev: observable,
  setLoading: action.bound,
  isLoading: observable,
});

const TransactionsTimelineStore = new Store();

export default TransactionsTimelineStore;


