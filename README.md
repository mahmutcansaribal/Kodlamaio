# Kodlamaio Python Selenium Öğrenimi

Bu kursta python yazılım dili kullanılarak test işlemleri öğrenilecektir.

#Python Pytest Dece

@pytest.mark.filterwarnings(...) -> İsteğe bagli alanlar atlanabilir.
@def test_foo(self):

@pytest.mark.skip() -> Bir test işlevinin atlatılmasını saglar.
@def test_the_unknown(self):

@pytest.mark.skipif(....) -> Bir sınıfın ya da modülün tüm test işlevlerini atlar.
class TestClass:
  def testFunc(self):
  
@pytest.mark.dependency() -> Testler arasındaki bagımlılıkları belirler.
def testLogin():
@pytest.mark.dependecy(depends=["testLogin"])
def testLogOut():


@pytest.mark.timeout() -> Testin belirli bir süre içerisinde tamamlanması gerektiğini belirler. Eğer test zamanında bitirilemezse başarısız olur.

@pytest.mark.parametrize(...) -> Aynı testın farklı parametreler ile çalışmasını saglar clean kod mimarisine de uygundur.

@pytest.fixture() --> Bir test fonksiyonuna veya sınıfına nesneler saglar. Test senaryolarının gerçek dünyaya simüle eder. Bir veritabanı baglantisi, dosya yolu veya bir nesne olusturmak icin kullanılır.

@pytest.fixture
def TestUser():
  return{'name':'Can', 'Surname':'Saribal'}
