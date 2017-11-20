# 关于addtion_phase子项目说明

## 初始化集群状态

**注意：** 此处初始化集群状态采用的 `cm` branch 的 `cmbbo/main.py/initialize_population(popu1, size, num_var)`方法，故此处所有说明，均适用于其方法说明。

- `make_population(popu1, size, num_var)`
为了便于构造初始集群，在构造集群所有参数的字典类型时，*按照容器的数量指定了VM、HM的数量，即`num_var`*；因此，在`population0`字典中，*所有的VM、HM都被指定了编号（包括running，down VM/HM）*。

- `initialize_population(popu1, size, num_var)`
构造代表集群状态的字典数据结构时，`population`字段记录了docker-(vm, hm)的映射，以及该映射造成的VM、HM实际使用掉的资源 `v_p_cost`、`v_m_cost`、`h_p_cost`、`h_m_cost`；对于实际没有被任何容器使用的VM，其对应`v_p/m_cost` 仍旧为 `0.0`，但是其资源尺寸，在初始化时已经设定了大小`v_rp`、`v_rm`。

- 总结
字典中`v_p_cost`、`v_m_cost`、`h_p_cost`、`h_m_cost`字段为 `0.0`，则说明该VM/HM down（not running），在计算集群的负载均衡方差时，应该以所有 `running vms/hms` 作为 计算对象，排除掉所有 `down vms/hms`，最好的方式应该是依据 `population` 字段指出的映射关系作为计算对象。