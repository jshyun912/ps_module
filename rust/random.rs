fn randint(min: u64, max: u64) -> u64
{
    static mut X: u64 = 0;

    unsafe 
    {
        while X == 0 { std::arch::asm!("rdrand rax", out("rax") X) }

        X ^= X << 13;
        X ^= X >> 7;
        X ^= X << 17;

        (X as u128 * (max - min + 1) as u128 / ((1_u128) << (64_u128)) + min as u128) as u64
    }
}

fn randfloat() -> f64 { randint(0, 9007199254740991) as f64 / 9007199254740992.0 }
