require 'minitest/autorun'

# fibo() 0 1 2 3 4 5 6  
# donne  1 1 2 3 5 8 13

class TestFibo < Minitest::Test

	def test_fibo
		assert_equal 1, fibo(0)
		assert_equal 1, fibo(1)
		assert_equal 2, fibo(2)
		assert_equal 3, fibo(3)
		assert_equal 5, fibo(4)
		assert_equal 8, fibo(5)
		assert_equal 13, fibo(6)
	end

end


def fibo(chiffre)

    if chiffre == 0
		return 1
	elsif chiffre == 1
		return 1
	end

    a = 1
    b = 1
    c = 2
    i = 2

    while i < chiffre do
    	a = b
    	b = c
    	c = a + b
    	i = i + 1
	end

	return c

end
