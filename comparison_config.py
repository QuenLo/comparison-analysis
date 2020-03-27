# EPA-Station Configuration
# --------------------------------------------------
# kick off over 2 km (check out EPA-info.csv)

HANDS_SITES = {
    "nantou"    : ['EPA-Nantou'     ,'74DA38C7CEDE', '74DA38E2B6C4'],
    "chiayi"    : ['EPA-Chiayi'     ,'74DA38B0522C', '74DA38C7CEB8'], # Chiayi
    "puzi"      : ['EPA-Puzi'       ,'74DA38ED0598', '74DA38C7D09A'],
    "keelung"   : ['EPA-Keelung'    ,'74DA38F2098E', '74DA38F20972', '74DA38EBF94A', '74DA38EBF952'],
    "yilan"     : ['EPA-Yilan'      ,'74DA38E2B492', '74DA38F2088A'],
    "hengchun"  : ['EPA-Hengchun'   ,'74DA38B05096' ], 
    "pingtung"  : ['EPA-Pingtung'   ,'74DA38F20CD6', '74DA38F20CD4'],
    "changhua"  : ['EPA-Changhua'   ,'74DA38AF476E', '74DA3895C436', '74DA38AF4824'],
    "banqiao"   : ['EPA-Banqiao'    ,'74DA38AF47CE', '74DA38AF4738', '74DA38EBF892', '74DA38EBF82A'],
    "xizhi"     : ['EPA-Xizhi'      ,'74DA388FF600', '74DA38F7C53A'],
    "hsinchu"   : ['EPA-Hsinchu'    ,'74DA38C7D38E', '74DA38C7D102', '74DA38C7D610'],
    "zhudong"   : ['EPA-Zhudong'    ,'74DA38F20948', '74DA38F2102E'],
    "pingzhen"  : ['EPA-Pingzhen'   ,'74DA38C7D15A', '74DA38E69DD2', '74DA38E2B4E2'],
    "taoyuan"   : ['EPA-Taoyuan'    ,'74DA38C7D07C', '74DA38C7D0D6', '74DA38AF473A', '74DA38E69E68'],
    "magong"    : ['EPA-Magong'     ,'74DA38F20D80', '74DA38F20F90'], # Penghu
    "zhongming" : ['EPA-Zhongming'  ,'74DA38AF47E6', '74DA3895C5DC', '74DA38E69CA0'],
    "fengyuan"  : ['EPA-Fengyuan'   ,'74DA3895C590', '74DA38AF498A', 'FT1_0447A', '74DA3895C4C6'],
    "yangming"  : ['EPA-Yangming'   ,'74DA38F7C486'],
    "wanhua"    : ['EPA-Wanhua'     ,'74DA38C7D398', '74DA38EBF86C', '74DA38EBF8C4', '74DA38C7D3A0', '74DA38EBF87C'],
    "shilin"    : ['EPA-Shilin'     ,'28C2DDDD45E0', '74DA38AF4798', '74DA38B051FE', '74DA38C7D476'],
    "tainan"    : ['EPA-Tainan'     ,'74DA38AF4746', '74DA3895DF40'], # Tainan
    "xinying"   : ['EPA-Xinying'    ,'74DA38C7D3F4', '74DA38C7D002', '74DA3895C274', 'G00000000011'],
    "taitung"   : ['EPA-Taitung'    ,'74DA38EBF89A', '74DA38F210F6'],
    "hualien"   : ['EPA-Hualien'    ,'74DA38EBF88E', '74DA38ED053E', '74DA38EBF8C2'],
    "sanyi"     : ['EPA-Sanyi'      ,'74DA38F208F0', '74DA38EBF8F0'],
    "miaoli"    : ['EPA-Miaoli'     ,'74DA38F207E8', '74DA38E69E98', '74DA38F20B98'],
    "matsu"     : ['EPA-Matsu'      ,'74DA38F2118E'],
    "kinmen"    : ['EPA-Kinmen'     ,'74DA38ED0424', '74DA38B05110'], # Kinmen
    "douliu"    : ['EPA-Douliu'     ,'74DA38AF495C', 'FT_LIVE3895C2D4'],
    "qianjin"   : ['EPA-Qianjin'    ,'74DA38AF486A', '74DA38AF4728', '74DA38F20E0E'],
    "meinong"   : ['EPA-Meinong'    ,'74DA38F21032', '74DA38F20E3A', '74DA38E69D88'],
    "banqiao_new"   : ['EPA-Banqiao'    ,'08BEAC028A4E', '08BEAC0286CE'], #update
    "taoyuan_new"   : ['EPA-Taoyuan'    ,'08BEAC028A74', '08BEAC0286E0'], # Update
    "zhongming_new" : ['EPA-Zhongming'  ,'08BEAC0286DC', '08BEAC0286DE'], # Update
    "wanhua_new"    : ['EPA-Wanhua'     ,'08BEAC028A52', '08BEAC028690'], # Update
    "tainan_new"    : ['EPA-Tainan'     ,'08BEAC0286B8', '08BEAC0286C8'], # Update
    "qianjin_new"   : ['EPA-Qianjin'    ,'08BEAC028770', '08BEAC028772'] # Update
}

NORTH_SITES = [ "keelung", "xinying", "banqiao", "shilin", "wanhua", "taoyuan", "pingzhen", "yangming" ]
CHU_MIAO_SITES = [ "zhudong", "hsinchu", "miaoli", "sanyi" ]
CENTRAL_SITES = [ "fengyuan", "zhongming", "changhua", "nantou" ]
YUN_CHIA_NAN_SITES = [ "douliu", "puzi", "chiayi", "xinying", "tainan" ]
KAO_PING_SITES = [ "meinong", "qianjin", "pingtung", "hengchun" ]
YILAN_SITES = [ "yilan" ]
HUA_TUNG = [ "taitung", "hualien" ]
ISLAND = [ "matsu", "kinmen", "magong" ]

NEW_SITES = [ "banqiao", "taoyuan", "zhongming", "wanhua", "tainan", "qianjin" ]


# Algorithm Configuration
# --------------------------------------------------
DAYS = [7,14,21,30]
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
#'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'spline', 'barycentric', 'polynomial', 'lagrange', 'linear'
INTERPOLATE_METHOD = "linear"

FEATURES_METHOD = {'ALL':['HUM','TEM','PM25','HR'], 'HUM':['HUM','PM25'], 'TEM':['TEM','PM25'], 'HR':['HR', 'PM25'], 'PM25':['PM25']}
LINEAR_METHOD = ['PassiveAggressiveRegressor','TheilSenRegressor','LinearRegression','BayesianRidge']
TEST_SIZE = 0.2
