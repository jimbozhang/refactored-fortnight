```python
from fetch_data_to_files import fetch_stock_id_names
from search_stock_in_pattern import make_report

from paths import STOCK_IDS_CSV, VOL_CSVS_DIR
```


```python
ids = fetch_stock_id_names(STOCK_IDS_CSV)
```


```python
report = make_report(ids, VOL_CSVS_DIR, time=None)
```


```python
report.iloc[1:30, :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>股票代码</th>
      <th>股票名称</th>
      <th>目标倍数</th>
      <th>昨天最高成交</th>
      <th>今天第一分钟成交</th>
      <th>昨日收盘价</th>
      <th>今日开盘价</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2728</th>
      <td>sh688016</td>
      <td>心脉医疗</td>
      <td>15.447236</td>
      <td>199</td>
      <td>3074</td>
      <td>143.24</td>
      <td>154.55</td>
    </tr>
    <tr>
      <th>1118</th>
      <td>sh688185</td>
      <td>康希诺</td>
      <td>13.737201</td>
      <td>293</td>
      <td>4025</td>
      <td>127.20</td>
      <td>143.33</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>sz002998</td>
      <td>优彩资源</td>
      <td>10.717579</td>
      <td>1735</td>
      <td>18595</td>
      <td>7.54</td>
      <td>7.71</td>
    </tr>
    <tr>
      <th>1761</th>
      <td>sh688108</td>
      <td>赛诺医疗</td>
      <td>10.424282</td>
      <td>766</td>
      <td>7985</td>
      <td>5.87</td>
      <td>6.11</td>
    </tr>
    <tr>
      <th>3806</th>
      <td>sz002598</td>
      <td>山东章鼓</td>
      <td>8.598077</td>
      <td>3640</td>
      <td>31297</td>
      <td>9.99</td>
      <td>10.98</td>
    </tr>
    <tr>
      <th>4374</th>
      <td>sz002104</td>
      <td>恒宝股份</td>
      <td>7.613105</td>
      <td>9447</td>
      <td>71921</td>
      <td>8.29</td>
      <td>7.45</td>
    </tr>
    <tr>
      <th>587</th>
      <td>sh688277</td>
      <td>天智航</td>
      <td>7.425971</td>
      <td>824</td>
      <td>6119</td>
      <td>13.49</td>
      <td>14.10</td>
    </tr>
    <tr>
      <th>1465</th>
      <td>sz300003</td>
      <td>乐普医疗</td>
      <td>7.298768</td>
      <td>4301</td>
      <td>31392</td>
      <td>19.30</td>
      <td>20.00</td>
    </tr>
    <tr>
      <th>321</th>
      <td>sz002498</td>
      <td>汉缆股份</td>
      <td>7.025416</td>
      <td>8656</td>
      <td>60812</td>
      <td>4.23</td>
      <td>4.38</td>
    </tr>
    <tr>
      <th>4181</th>
      <td>sh600216</td>
      <td>浙江医药</td>
      <td>6.585885</td>
      <td>3004</td>
      <td>19784</td>
      <td>14.11</td>
      <td>14.43</td>
    </tr>
    <tr>
      <th>4311</th>
      <td>sh600196</td>
      <td>复星医药</td>
      <td>6.399855</td>
      <td>4144</td>
      <td>26521</td>
      <td>40.70</td>
      <td>37.08</td>
    </tr>
    <tr>
      <th>3113</th>
      <td>sh600784</td>
      <td>鲁银投资</td>
      <td>6.352242</td>
      <td>1093</td>
      <td>6943</td>
      <td>7.64</td>
      <td>7.90</td>
    </tr>
    <tr>
      <th>404</th>
      <td>sz001259</td>
      <td>利仁科技</td>
      <td>6.285068</td>
      <td>221</td>
      <td>1389</td>
      <td>34.41</td>
      <td>37.85</td>
    </tr>
    <tr>
      <th>639</th>
      <td>bj871245</td>
      <td>威博液压</td>
      <td>6.000000</td>
      <td>10</td>
      <td>60</td>
      <td>12.44</td>
      <td>12.60</td>
    </tr>
    <tr>
      <th>2609</th>
      <td>sh688029</td>
      <td>南微医学</td>
      <td>5.779720</td>
      <td>286</td>
      <td>1653</td>
      <td>77.20</td>
      <td>81.97</td>
    </tr>
    <tr>
      <th>4371</th>
      <td>sz000597</td>
      <td>东北制药</td>
      <td>5.693689</td>
      <td>2060</td>
      <td>11729</td>
      <td>5.15</td>
      <td>5.23</td>
    </tr>
    <tr>
      <th>4597</th>
      <td>sh603021</td>
      <td>山东华鹏</td>
      <td>5.519656</td>
      <td>12541</td>
      <td>69222</td>
      <td>5.71</td>
      <td>6.06</td>
    </tr>
    <tr>
      <th>2390</th>
      <td>sh600875</td>
      <td>东方电气</td>
      <td>5.295265</td>
      <td>12250</td>
      <td>64867</td>
      <td>19.93</td>
      <td>21.02</td>
    </tr>
    <tr>
      <th>930</th>
      <td>bj833819</td>
      <td>颖泰生物</td>
      <td>5.132000</td>
      <td>500</td>
      <td>2566</td>
      <td>5.53</td>
      <td>5.60</td>
    </tr>
    <tr>
      <th>1696</th>
      <td>sh603458</td>
      <td>勘设股份</td>
      <td>4.931200</td>
      <td>625</td>
      <td>3082</td>
      <td>10.21</td>
      <td>10.10</td>
    </tr>
    <tr>
      <th>2528</th>
      <td>sz300529</td>
      <td>健帆生物</td>
      <td>4.643794</td>
      <td>991</td>
      <td>4602</td>
      <td>47.96</td>
      <td>48.96</td>
    </tr>
    <tr>
      <th>806</th>
      <td>bj836239</td>
      <td>长虹能源</td>
      <td>4.625000</td>
      <td>80</td>
      <td>370</td>
      <td>30.80</td>
      <td>32.39</td>
    </tr>
    <tr>
      <th>988</th>
      <td>sz002828</td>
      <td>贝肯能源</td>
      <td>4.499066</td>
      <td>6957</td>
      <td>31300</td>
      <td>8.25</td>
      <td>8.70</td>
    </tr>
    <tr>
      <th>619</th>
      <td>sz002901</td>
      <td>大博医疗</td>
      <td>4.373134</td>
      <td>134</td>
      <td>586</td>
      <td>33.20</td>
      <td>33.95</td>
    </tr>
    <tr>
      <th>3496</th>
      <td>sz300228</td>
      <td>富瑞特装</td>
      <td>4.328891</td>
      <td>5853</td>
      <td>25337</td>
      <td>6.00</td>
      <td>6.25</td>
    </tr>
    <tr>
      <th>910</th>
      <td>sz002843</td>
      <td>泰嘉股份</td>
      <td>4.252412</td>
      <td>1244</td>
      <td>5290</td>
      <td>18.32</td>
      <td>18.49</td>
    </tr>
    <tr>
      <th>1037</th>
      <td>sz301321</td>
      <td>翰博高新</td>
      <td>4.189222</td>
      <td>1633</td>
      <td>6841</td>
      <td>24.23</td>
      <td>24.90</td>
    </tr>
    <tr>
      <th>3913</th>
      <td>sh600256</td>
      <td>广汇能源</td>
      <td>4.156700</td>
      <td>31806</td>
      <td>132208</td>
      <td>12.64</td>
      <td>13.15</td>
    </tr>
    <tr>
      <th>4183</th>
      <td>sz002551</td>
      <td>尚荣医疗</td>
      <td>4.012625</td>
      <td>2297</td>
      <td>9217</td>
      <td>4.23</td>
      <td>4.24</td>
    </tr>
  </tbody>
</table>
</div>


