type Coord = (i64, i64);

fn ccw(a:Coord, b:Coord, c:Coord) -> i64 { (b.0 - a.0) * (c.1 - b.1) - (b.1 - a.1) * (c.0 - b.0) }

fn convex_hull(a:&Vec<Coord>) -> Vec<Coord>
{
    let mut ans:Vec<Coord> = vec![];

    let (mut up, mut down):(Vec<Coord>, Vec<Coord>) = (vec![], vec![]);

    for i in a
    {
        while up.len() >= 2 && ccw(up[up.len() - 2], up[up.len() - 1], *i) >= 0 { up.pop().unwrap(); }
        up.push(*i)
    }

    for i in a.iter().rev()
    {
        while down.len() >= 2 && ccw(down[down.len() - 2], down[down.len() - 1], *i) >= 0 { down.pop().unwrap(); }
        down.push(*i)
    }

    for i in down.iter().rev().take(down.len() - 1) { ans.push(*i) }
    for i in up.iter().rev().take(up.len() - 1) { ans.push(*i) }

    ans
}
