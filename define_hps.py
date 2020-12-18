my_hps = Hp()
hp_1 = my_hps.numrange(name='num_nodes_hidd_1', min=32, max=256, type='int')
hp_2 = my_hps.numrange(name='num_nodes_hidd_1', min=32, max=256, type='int')
hp_3 = my_hps.numrange(name='lr', min=0.0001, max=0.01, type='log')
