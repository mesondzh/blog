---
title: 了解门罗币
date: 2018-08-21 23:29:08
updated: 2018-08-21 23:29:08
description: 介绍门罗币的相关基础知识。
categories: 
- 区块链
type: photo
photos:
- https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821112307.png
tags: 
- XMR
- 门罗币
- 区块链 
music-id: 5308001
---

> 参考：[《区块链教程》](https://liuchengxu.gitbooks.io/blockchain-tutorial/content/)

根据 [Monero（门罗） 官网](https://getmonero.org/): Monero 是一个安全，隐私和不可追踪的加密货币。通过使用密码学中一种特殊的方法，门罗确保了所有交易保持 100% 的不可关联和不可追溯性(unlinkable and untraceable)。

尽管 bytecoin 十分有前景，但是人们也注意到发生了很多负面的事情，并且鉴于它已经产出了 80% 的币。所以，决定将 bytocin 分叉，新链上的币叫做 Bitmonero，最终被重新命名为 Monero（门罗），在世界语（Esperanto）中叫做“coin”，硬币的意思。门罗的出块时间为两分钟。

门罗由一个 7 人的开发者团队领导，其中 5 人匿名，另 2 人已公开。他们是 David Latapie 和 Riccardo Spagni aka “Fluffypony”。项目是开源众筹的形式进行。

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821100611.jpg)

## 门罗的特别之处

门罗采用CrytoNote算法，使得它具有以下几个特性。

* 你的钱就是你的：你对交易有着绝对的控制权。你为你的钱负责。因为你的身份是私有的（private），没有人能够看到你把钱花到了哪儿。
* 可替代性：所谓可替换性，指的是一个商品或资产与其他同类型个体商品或资产的互换性。

加密货币中理想的可替代性是什么？

> 以 [bitcoin](https://blockgeeks.com/guides/what-is-bitcoin-a-step-by-step-guide/) 为例，它引以为豪的一点就是比特币是开放的账本，但是，这也意味着每个人都可以看到里面的每一笔交易，更重要的是，每个人都可以看到交易的踪迹。简单来说，如果你拥有一个曾经用于某个非法交易的比特币，比如购买毒品，那么它的交易细节里面将会永远有这样的印记。实际上，这“污染（taint）”了你的比特币。
>
> 在某些比特币服务提供商和交易所中，这些“被污染”的币与“干净的”币永远都不会被一视同仁。这就泯灭了可替换性（fungibility），这也是比特币经常为人所诟病的一点。毕竟，为什么别人做了错事，需要你来买单呢？

于是门罗诞生了。由于所有数据和交易都是不公开的，没有人能够知道你的门罗币在之前经历了哪些交易，也无法知道你的门罗币会用来购买什么。

* 动态扩展性：比特币协议限定了区块大小为 1 Mb（译者注：扩容，BCH 等为后话）。在早期，比特币并没有任何区块大小的限制，但是后来为了防止垃圾交易，就施加了大小限制。门罗并没有任何“预先设定”的限制，系统有一个区块奖励的惩罚（block reward penalty）。工作方式如下：
  * 首先，最后 100 个区块大小的中位数叫做 M100。假设矿工挖出了一个新的块，大小记为 NBS（New Block Size）。如果 NBS > M100，那么区块奖励会随着 NBS 超过 M100 的平方递减。
  * 也就是说，如果 NBS 大于 M100 [10%, 50%, 80%, 100%]，那么区块奖励随之减少 [1%, 25%, 64%, 100%]. 通常来说，区块大小超过 2 倍的 M100 是不被允许的，同时如果区块小于等于 60kb 则会免于任何的区块奖励惩罚。

* 防 ASIC：门罗不算是严格的“ASIC resistant”，但是制作针对门罗的 ASIC 将会成本高昂，以至于不值得如此操作。当我们说门罗基于 CryptoNote 系统时，已经使得它与比特币截然不同。在基于 CtryptoNote 的系统中所用的哈希算法叫做 "CryptoNight"。
  * 创造 Cryptonight 是为了构建一个更加公平，更加去中心化的货币系统。利用 cryptonight 的加密货币无法用 ASIC 挖矿。它的目的是希望可以杜绝出现矿池的出现，并使得货币分散地更均匀。
  * Crytponight 需要 2 MB 的快速内存来工作。这意味着并行哈希会被一个芯片可以分配多少内存限制，同时保持尽可能地低成本，以免“入不敷出”。2 MB 的内存要比 SHA256 电路要耗费多得多的硅。
  * Cryptonight 是 CPU 和 GPU 友好型，因为它利用了 AES-Ni 指令集。基本上，如果你用的是没那么老的机器，由 Cryptonight 所完成的一些工作已经在硬件层完成。
  * 已经有不少说法说，想要把门罗从工作量证明算法切换至“Cuckoo Cycle”（一种不同于工作量证明的哈希）。如果这种切换真的发生，那么在 R&D 门罗 ASIC 友好型所耗费的所有工作都将付之东流。

* 多密钥：
  * **view key：门罗有一个 public view key 和 private view key。**public view key 用于生成一次性的 stealth public address(隐匿的公开地址)，资金将会通过这个地址发送给接收者。private view key 用于接收者扫描区块链来找到发送给他们的资金。
  * **spend key： 如果 view key 大多是为了交易接收方，那么 spend key 就是全部有关于发送方。跟上面一样，有两个 spend key：public spend key 和 private spend key。**public spend key 帮助发送方参与环交易（ring transaction），并验证密钥镜像(key image)的签名。private spend key 帮助创建密钥镜像，密钥镜像能够使得他们能够发送交易。
  * 门罗地址是一个 95 个字符的字符串，分别由 public spend key 和 public view key 构成。

##  加密货币交易的工作方式

假设 Alice 需要给 Bob 发送一些比特币，交易看起来是怎样的？

###  交易输入

每个币都来源于之前的交易。所以，Alice 可以将之前交易的输出作为新交易的输入。Alice 需要从下列交易从获得输入，比如 TX(0), TX(1) 和 TX(2)。这三笔交易会被一起包含到这笔交易，并有一个交易输出 TX(Input)。

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821102809.png)

### 交易输出

输出就是 Bob 可以在之后交易花费的钱，也可能会出现找零，找零会返回给 Alice。找零会成为 Alice 未来任意交易的输入。

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821102931.png)

有了公钥加密以后，比特币交易才成为可能。为了对它有一个基本的理解，请看下图：

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821103045.png)

比特币用户首先选择私钥，公钥由私钥衍生而来。将公钥进行哈希得到一个公开的地址公布出去。如果 Alice 要给 Bob 发送 BTC，Alice 直接给 Bob 公开的地址发送即可。

门罗团队给出的“电子现金三角（Electronic cash triangle）”

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821103218.png)

正如他们所说，一个理想的电子现金应该满足三个前提：**电子的、去中心化的、隐私的**

门罗背后的哲学就是完全隐私和不透明性。发送方隐私由环签名（Ring Signature）实现。

* Ring Signatures(环签名)保证了发送方隐私
* Condidential Address(隐匿地址)保证了接收方隐私
* Ring CT(Ring Confidential Transaction, 环隐匿交易)保证了交易隐私

## 门罗密码学

### Ring Signatures

环签名，简单来说就是交易过程中把几个人签名混合在一起，然后得到一个独一无二的签名，这样就没人知道这个签名是否是你本人的。

假设，Alice 发送 1000 XMR(XMR 即门罗币) 给 Bob，系统会如何使用环签名来隐藏她的身份？

首先，Alice 会确认她的“ring size（环大小）”。ring size 是取自区块链的随机输出，它等于 Alice 的输出值，即 1000 XMR。ring size 越大，交易越大，继而交易费越高。然后，她用 private spend key 对输出进行签名，并发给到区块链。另一点要注意的是，Alice 不需要向之前交易的所有者发送请求来使用这些输出。

假设 Alice 选择的 ring size 为 5 ，也就是说 4 个 decoy output（诱骗输出） 和它自己的交易，从外面看起来就像这样：

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821104337.png)

在一个环签名交易中，任意一个 decoy 就像真实输出一样，因为任何不相关的第三方（包括矿工）都无法知道发送方是谁。

**防止双花：**

矿工要做的一个重要的事情就是防止“双花”。双花就是指在同一时间，同一笔钱出现在两笔，甚至更多的交易中。双花被矿工所解决。在一个区块链中，只有当矿工将交易包含在区块并出块，交易才算完成。假设 A 打算给 B 发送一个比特币，然后它发送同样一个币给 C，矿工会把其中一笔交易放到块里，并在处理过程中覆盖另一笔交易，防止双花。但是在门罗中，由于环签名这些都是不可见的。那么要如何防止双花呢？

门罗的每一笔交易都有它自己的唯一的**密钥镜像（key image）**，鉴于密钥镜像对于每个交易都是不同的，矿工就可以非常容易地检测，判断是否双花。

### stealth address

门罗的最大一个卖点就是交易的不可关联性（unlinkability）。基本上，如果有人发送给你 200 XMR，应该没有人知道这笔钱是发送给你的。如果 Alice 要给 Bob 发送门罗币，除了 Alice，应该没人任何人知道 Bob 就是这笔钱的接收者。

**门罗要如何保证 Bob 的隐私？**

Bob 有两个 public key：public view key 和 public send key。为了推进交易，Alice 的钱包会用 Bob 的 public view key 和 public send key 来生成一次性独一无二的 public key。

**one-time public key （P） 的计算方式：** $ P = H(rA)G + B $

其中：

- r = Random scalar chosen by Alice. Alice 选取的一个随机的标量
- A = Bob’s public view key. Bob 的 public view key
- G = Cryptographic constant. 密码学常数
- B = Bob’s public spend key. Bob 的 public spend key
- H() = The Keccak hashing algorithm used by Monero. 门罗所使用的 Keccak 哈希算法

由这种方法生成一次性公钥，然后再生成在区块链里一次性的公开地址，这样的地址就叫做“stealth address”，Alice 就通过它给 Bob 发送门罗币。现在，Bob 要如何从数据的随机分布中解锁收到的门罗币呢?

Bob 也有一个 private spend key。private spend key 就是用来帮助 Bob 扫描区块链找到他的相关交易。当 Bob 找到这笔交易，他可以通过一个 private key 取回他的门罗币，这个 private key 与一次性的 public key 相关。因此 Alice 付给 Bob 门罗币，无人知晓。

**key image**

计算方式：$I = xH(P)$ 

* x 为发送方的 private spend key
* P是one-time public key

从 key image "I" 计算出一次性的 public address P 十分困难(这是密码学哈希函数的一个属性，正着算很容易，反推很难)，因此 Alice 的身份永远也不会暴露。

当 P 被哈希的时候，永远都会返回同一个值，意味着 H(P) 也总是同一个值。既然 x 的值对于 Alice 来说是个常数，她也就是永远也无法生成多个 I 值。这使得 key image 对于每一笔交易都是不同的。

### Ring Confidential Transactions

基于 Gergory Maxwell 的研究实现了 Ring CT，Ring CT保证了交易本身的匿名性，它在链上隐藏了交易的数额。这也意味着所有的交易输入都不需要再被拆分为已知的面额，钱包现在可以从任意的 Ring CT 输出中选择 ring 成员。

环形加密技术的基础仍旧是与比特币一样的基于Hash值的公钥+私钥加解机制。只是比特币是用接受者的公钥加密，接受者用与之配对的私钥解密验证。而环形加密则使用了多个公钥进行加密，并用接受者的私钥进行解密验证。

####  Kovri and I2P

I2P 是一个路由系统，它能够让应用秘密地互相发送信息而无须任何外部干涉。Kovri 是 I2P 的 C++ 实现，它也会被集成到门罗里面。**Kovri 将会隐藏你的网络流量**，如此一来，被动的网络监控就根本不会暴露你正在使用门罗。为此，你的所有门罗流量将会被加密并通过 I2P 节点路由。节点就像瞎的看门人，它们会知道你的信息通过，但是**不知道这些去向哪儿以及信息的具体内容**。

###  门罗价值和市值

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821111312.jpg)

目前，XMR流通市值$1,522,148,966，流通量16,335,709 XMR每个XMR￥637，占全球总市场0.7%，排名10。门罗总量为 1840 万，挖矿奖励会持续到 2022 年 5 月 31。之后，系统设定为 0.3 XMR/min 的奖励。这是为了矿工能过持续的激励挖矿，而不仅仅依赖于交易费，毕竟门罗已经被挖完了。

### 门罗的优势与劣势

### 优势

- 隐私性最好的几个加密货币之一
- 交易之间不可联系
- 交易不可跟踪
- 区块链没有区块限制，并且可动态扩展
- 即使当门罗的供应耗尽，也会有 0.3 XMR/min 的供应量激励矿工
- 经济上已经获得了巨大增长
- 其透明性实可选的。如果有人想要交易对某些人可见，比如给审计人员查看密钥。这也使得门罗是可审计的加密货币。
- 有一个非常有能力的强大开发团队领导工作

### 劣势

- 尽管门罗已经被设计为防 ASIC 来避免中心化，但是门罗接近 43% 的算力仍然为 3 个矿池所有：

![](https://raw.githubusercontent.com/ds19991999/githubimg/master/picgo/20180821112000.png)

* 比起其他加密货币，由于涉及了很多的加密操作，门罗的交易大小要大得多。
* 门罗的钱包兼容性不强。事实上，门罗至今没有硬件钱包（截止成文之时）。
* 入门有难度，并且尚未被广泛接纳。
* 因为它并非是基于比特币的货币，门罗面临的问题是向其中加入一些元素相对更困难。

**毫无疑问，未来会更加开放和去中心化，门罗也会因其隐私性而越具吸引力。特别有趣之处在于，它是少数几个不是基于比特币的币，却是同时有着真正价值的“潜力股”。对门罗来说，随着它已经经历了惊人的增长，未来依旧光明一片。当实现 Kovri 以后，相信一切会变得更加有趣.**



**注：[cryptonote系统](https://github.com/cryptonotefoundation/cryptonote)、[monero](https://getmonero.org/)**

