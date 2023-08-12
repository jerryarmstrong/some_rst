src/v2/stores/nodes.js
======================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {filter, reject} from 'lodash/fp';
import {action, computed, decorate, observable, flow} from 'mobx';
import * as API from 'v2/api/stats';

class Store {
  network = [];

  updateClusterInfo = data => {
    if (typeof data === 'string') {
      data = JSON.parse(data);
    }
    this.network = data.network || [];
    this.totalStaked = data.totalStaked;
    this.totalStakedSol = data.totalStakedSol;
    this.supply = data.supply;
    this.networkInflationRate = data.networkInflationRate;
  };

  fetchClusterInfo = flow(function*() {
    try {
      const res = yield API.getClusterInfo();
      const data = res.data;
      this.updateClusterInfo(data);
      return res;
    } catch (e) {
      throw e;
    }
  });

  get validators() {
    return filter({what: 'Validator'})(this.network);
  }

  get activeValidators() {
    return filter('activatedStake')(this.validators);
  }

  get inactiveValidators() {
    return reject('activatedStake')(this.validators);
  }
}

decorate(Store, {
  network: observable,
  supply: observable,
  stakedTokens: observable,
  updateClusterInfo: action.bound,
  validators: computed,
  activeValidators: computed,
  inactiveValidators: computed,
  fetchClusterInfo: action.bound,
});

const NodesStore = new Store();
NodesStore.fetchClusterInfo();

export default NodesStore;


