import Test.HUnit

main = runTestTT (
	test [
	fibonacci 1 ~=? 1,
	fibonacci 2 ~=? 1,
	fibonacci 3 ~=? 2
	])

fibonacci 1 = 1
fibonacci 2 = 1
fibonacci 3 = 2

-- Paquets cabal-install haskell-platform ghs
-- apt-get install cabal-install; cabal update; cabal install; cabal install hunit
-- runhaskell test_fibo.hs ou runghc test_fibo.hs