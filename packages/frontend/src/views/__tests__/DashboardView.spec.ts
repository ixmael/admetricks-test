import {
    describe,
    it,
    expect,
} from 'vitest'

import { mount } from '@vue/test-utils'
import DashboardView from '../DashboardView.vue'

describe('DashboardView', () => {
  it('renders properly', () => {
    const wrapper = mount(DashboardView);

    expect(wrapper.find('.filters').exists()).toEqual(true);
    expect(wrapper.find('.datepicker').exists()).toEqual(true);
    expect(wrapper.find('.graph').exists()).toEqual(true);
    expect(wrapper.find('.download').exists()).toEqual(true);
    expect(wrapper.find('.linear-graph').exists()).toEqual(true);
  });
})
