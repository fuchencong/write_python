# algorithms

A project to practice algorithms with Python
Inspired by [keon/algorithms](https://github.com/keon/algorithms)

## arrays

### delete_nth

* 使用字典保存每个数出现的次数
* 使用 defaultdict 简化 key 不存在的处理逻辑

### flatten

* 递归问题，递归退出的条件：当前元素不是可迭代对象（需要排除字符串）
* 通过 isinstance(element, Iterable) 判断当前对象是否为可迭代对象，更好的方式是 iter(element)

### garage

* 算法题：当 0 的和最终位置不匹配时，此时直接选择一个完成交换
* 选择的 car 必须最终达到 final 位置，这样直接和 final 里相应位置的 car 交换
* 如果 0 的位置匹配，但没有达到 final 状态，就需要调整任意一个 car，重复上述逻辑

### josephus

* 环状数据结构，每隔 n 个移除元素问题，使用 % 计算需要移除的问题

### limit

* 使用列表推导计算新的列表，或者考虑使用 filter 高阶函数
