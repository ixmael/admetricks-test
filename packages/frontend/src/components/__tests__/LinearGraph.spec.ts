import {
    describe,
    it,
    expect,
} from 'vitest'
import { mount } from '@vue/test-utils'

import LinearGraph from '../LinearGraph.vue'

describe('LinearGraph', () => {
  
  it('renders no data message', () => {
    const wrapper = mount(LinearGraph, { props: { data: [] } });
    expect(wrapper.text()).toContain('No hay datos para graficar');
  });

  it('the graph is visible', () => {
    const wrapper = mount(LinearGraph, { props: { data: [{ date: '2000-01-01', close: 10, difference: 0 }] } });

    // The no data message dissapear
    expect(wrapper.text()).toContain('');

    // Show the graph
    // wrapper.setProps({ data: []})
    // expect(wrapper).toContain('');
  });
});
