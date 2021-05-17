
组件从概念上看就是一个函数，可以接受一个参数作为输入值，这个参数就是props，所以可以把props理解为从外部传入组件内部的数据。由于React是单向数据流，所以props基本上也就是从服父级组件向子组件传递的数据。

用法
假设我们现在需要实现一个列表，根据React组件化思想，我们可以把列表中的行当做一个组件，也就是有这样两个组件：<ItemList/>和<Item/>。

先看看<ItemList/>

import Item from "./item";
export default class ItemList extends React.Component{
  const itemList = data.map(item => <Item item=item />);
  render(){
    return (
      {itemList}
    )
  }
}
列表的数据我们就暂时先假设是放在一个data变量中，然后通过map函数返回一个每一项都是<Item item='数据'/>的数组，也就是说这里其实包含了data.length个<Item/>组件，数据通过在组件上自定义一个参数传递。当然，这里想传递几个自定义参数都可以。

在<Item />中是这样的：

export default class Item extends React.Component{
  render(){
    return (
      <li>{this.props.item}</li>
    )
  }
}
在render函数中可以看出，组件内部是使用this.props来获取传递到该组件的所有数据，它是一个对象，包含了所有你对这个组件的配置，现在只包含了一个item属性，所以通过this.props.item来获取即可。

只读性
props经常被用作渲染组件和初始化状态，当一个组件被实例化之后，它的props是只读的，不可改变的。如果props在渲染过程中可以被改变，会导致这个组件显示的形态变得不可预测。只有通过父组件重新渲染的方式才可以把新的props传入组件中。

默认参数
在组件中，我们最好为props中的参数设置一个defaultProps，并且制定它的类型。比如，这样：

Item.defaultProps = {
  item: 'Hello Props',
};

Item.propTypes = {
  item: PropTypes.string,
};
关于propTypes，可以声明为以下几种类型：

optionalArray: PropTypes.array,
optionalBool: PropTypes.bool,
optionalFunc: PropTypes.func,
optionalNumber: PropTypes.number,
optionalObject: PropTypes.object,
optionalString: PropTypes.string,
optionalSymbol: PropTypes.symbol,
注意，bool和func是简写。

这些知识基础数据类型，还有一些复杂的，附上链接：

https://facebook.github.io/react/docs/typechecking-with-proptypes.html

总结
props是一个从外部传进组件的参数，主要作为就是从父组件向子组件传递数据，它具有可读性和不变性，只能通过外部组件主动传入新的props来重新渲染子组件，否则子组件的props以及展现形式不会改变。

state
state是什么呢？

State is similar to props, but it is private and fully controlled by the component.

一个组件的显示形态可以由数据状态和外部参数所决定，外部参数也就是props，而数据状态就是state。

用法
export default class ItemList extends React.Component{
  constructor(){
    super();
    this.state = {
      itemList:'一些数据',
    }
  }
  render(){
    return (
      {this.state.itemList}
    )
  }
}
首先，在组件初始化的时候，通过this.state给组件设定一个初始的state，在第一次render的时候就会用这个数据来渲染组件。

setState
state不同于props的一点是，state是可以被改变的。不过，不可以直接通过this.state=的方式来修改，而需要通过this.setState()方法来修改state。

比如，我们经常会通过异步操作来获取数据，我们需要在didMount阶段来执行异步操作：

componentDidMount(){
  fetch('url')
    .then(response => response.json())
    .then((data) => {
      this.setState({itemList:item});  
    }
}
当数据获取完成后，通过this.setState来修改数据状态。

当我们调用this.setState方法时，React会更新组件的数据状态state，并且重新调用render方法，也就是会对组件进行重新渲染。

注意：通过this.state=来初始化state，使用this.setState来修改state，constructor是唯一能够初始化的地方。

setState接受一个对象或者函数作为第一个参数，只需要传入需要更新的部分即可，不需要传入整个对象，比如：

export default class ItemList extends React.Component{
  constructor(){
    super();
    this.state = {
      name:'axuebin',
      age:25,
    }
  }
  componentDidMount(){
    this.setState({age:18})  
  }
}
在执行完setState之后的state应该是{name:'axuebin',age:18}。

setState还可以接受第二个参数，它是一个函数，会在setState调用完成并且组件开始重新渲染时被调用，可以用来监听渲染是否完成：

this.setState({
  name:'xb'
},()=>console.log('setState finished'))
总结
state的主要作用是用于组件保存、控制以及修改自己的状态，它只能在constructor中初始化，它算是组件的私有属性，不可通过外部访问和修改，只能通过组件内部的this.setState来修改，修改state属性会导致组件的重新渲染。